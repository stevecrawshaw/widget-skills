# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Build the filters reference from the ngdocs partials.

The scraped widget documentation covers directives only. AngularJS filters and
the config service are documented solely in the online single-page app, whose
content lives in per-page HTML partials:

    js/docs-setup.js                     catalogue of every page
    partials/api/<id with : as .>.html   that page's body

Fetch with --fetch (needs network), then convert. Fetched partials are cached
under partials/ so a rebuild is offline.

Run: uv run scripts/build_filters.py --fetch
"""

from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "partials"
OUT = ROOT / "skill" / "reference" / "filters-and-config.md"
BASE = "https://help.opendatasoft.com/widgets/"
WANTED_TYPES = {"filter", "service", "object", "provider"}

TAG = re.compile(r"<[^>]+>")
ROW = re.compile(r"<tr>(.*?)</tr>", re.S)
CELL = re.compile(r"<td[^>]*>(.*?)</td>", re.S)


def text(fragment: str) -> str:
    """Strip tags, keeping inline code as backticks."""
    fragment = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", fragment, flags=re.S)
    return html.unescape(" ".join(TAG.sub(" ", fragment).split())).strip()


def rich_text(fragment: str) -> str:
    """Like text(), but keeps block structure: headings, lists, code blocks.

    Filter descriptions are a sentence or two, so text() suffices for them.
    The config pages are long enough that flattening them to one paragraph
    makes them unreadable.
    """
    # Lift code blocks out first and hold them aside. Later passes strip
    # tags, and an unescaped "<your token>" inside a code block would look
    # exactly like one.
    blocks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        body = html.unescape(TAG.sub("", match.group(1))).strip()
        blocks.append(body)
        return f"\n\n\x00{len(blocks) - 1}\x00\n\n"

    out = re.sub(r"<pre[^>]*>(.*?)</pre>", stash, fragment, flags=re.S)
    out = re.sub(r"<h(\d)[^>]*>(.*?)</h\1>",
                 lambda m: "\n\n" + "#" * (int(m.group(1)) + 1) + " "
                 + text(m.group(2)) + "\n\n", out, flags=re.S)
    out = re.sub(r"<li[^>]*>(.*?)</li>",
                 lambda m: "\n- " + text(m.group(1)), out, flags=re.S)
    out = re.sub(r"</p>", "\n\n", out)
    out = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", out, flags=re.S)
    out = html.unescape(TAG.sub("", out))
    out = re.sub(r"[ \t]+", " ", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    out = "\n".join(line.strip() for line in out.splitlines()).strip()
    for n, body in enumerate(blocks):
        out = out.replace(f"\x00{n}\x00", f"\n\n```json\n{body}\n```\n")
    return out.strip()


def fetch() -> None:
    CACHE.mkdir(exist_ok=True)
    req = urllib.request.Request(BASE + "js/docs-setup.js",
                                 headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
    pages = [p for p in data["pages"]
             if p["section"] == "api" and p["type"] in WANTED_TYPES]
    for page in pages:
        name = page["id"].replace(":", ".") + ".html"
        target = CACHE / name
        if target.exists() and target.stat().st_size:
            continue
        req = urllib.request.Request(BASE + "partials/api/" + name,
                                     headers={"User-Agent": "Mozilla/5.0"})
        target.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        time.sleep(0.3)
    print(f"cached {len(pages)} partials in {CACHE}")


def section(body: str, heading_id: str) -> str:
    """The div whose class matches the heading, e.g. 'description'."""
    match = re.search(
        rf'<div class="{heading_id}">(.*?)</div>\s*</div>', body, re.S
    )
    return match.group(1) if match else ""


def params(body: str) -> list[tuple[str, str, str]]:
    table = re.search(r'<table class="variables-matrix table.*?</table>',
                      body, re.S)
    if not table:
        return []
    rows = []
    for row in ROW.findall(table.group(0)):
        cells = CELL.findall(row)
        if len(cells) == 3:
            rows.append(tuple(text(c) for c in cells))
    return rows


def returns(body: str) -> str:
    match = re.search(
        r'id="usage_in-javascript_returns".*?<table[^>]*>(.*?)</table>',
        body, re.S)
    if not match:
        return ""
    cells = CELL.findall(match.group(1))
    if len(cells) == 2:
        return f"`{text(cells[0])}` — {text(cells[1])}"
    return " ".join(text(c) for c in cells)


def convert(path: Path) -> tuple[str, str, str, str]:
    body = path.read_text(encoding="utf-8")
    name_match = re.search(r"<h1><code[^>]*>(.*?)</code>", body, re.S)
    name = text(name_match.group(1)) if name_match else path.stem
    kind_match = re.search(r'<span class="hint">(\w+) in module', body)
    kind = kind_match.group(1) if kind_match else "filter"

    binding = re.search(
        r'<div class="in-html-template-binding">(.*?)</div>', body, re.S)
    # The partial already wraps the expression in {{ }}; text() adds backticks
    # around the <code>, so take them back off.
    usage = text(binding.group(1)).strip("`").strip() if binding else ""

    description = rich_text(section(body, "description"))
    if not description:
        # Filters put their prose in the Returns cell instead.
        description = returns(body)

    parts: list[str] = [f"## {name}", ""]
    if usage:
        parts += ["```html", usage, "```", ""]
    if description:
        parts += [description, ""]
    rows = params(body)
    if rows:
        parts += ["| Parameter | Type | Details |", "|---|---|---|"]
        parts += [f"| `{n}` | {t} | {d} |" for n, t, d in rows]
        parts.append("")
    ret = returns(body)
    if ret and ret != description:
        parts += [f"**Returns** {ret}", ""]
    return name, kind, usage, "\n".join(parts)


PREAMBLE = """\
# Filters and configuration

A **filter** transforms a value inside a `{{ }}` binding, after a pipe:

```html
{{ record.fields.price | number:2 }}
{{ record.fields.name | capitalize }}
{{ record.fields.tags | join:', ' }}
```

Filters chain left to right, and arguments follow the name after colons:

```html
{{ record.fields.description | truncate:80 | capitalize }}
```

They work only inside bindings and in `ng-repeat` expressions. They cannot be
used in a widget's own attributes, because those are parsed by the widget
rather than by AngularJS.

## AngularJS built-in filters

These ship with AngularJS itself, not with ods-widgets, so they are absent
from the widget documentation. They are the ones you reach for most.

| Filter | Example | Effect |
|---|---|---|
| `number` | `{{ n \\| number }}` | Thousands separators. `number:1` fixes one decimal place |
| `date` | `{{ d \\| date:'dd/MM/yyyy' }}` | Formats a date or datetime |
| `currency` | `{{ v \\| currency:'£' }}` | Currency symbol and two decimals |
| `uppercase` / `lowercase` | `{{ s \\| uppercase }}` | Case conversion |
| `limitTo` | `{{ items \\| limitTo:5 }}` | First n items of an array or string |
| `orderBy` | `ng-repeat="r in rows \\| orderBy:'-count'"` | Sorts; `-` reverses |
| `json` | `{{ obj \\| json }}` | Pretty-prints an object. Useful for debugging a binding |

`{{ value | json }}` is the fastest way to find out what a widget actually put
into scope when a binding renders blank.

## ods-widgets filters
"""


def main() -> int:
    if "--fetch" in sys.argv:
        fetch()
    if not CACHE.exists() or not any(CACHE.glob("*.html")):
        print("no cached partials; run with --fetch", file=sys.stderr)
        return 1

    filters: list[tuple[str, str, str]] = []
    services: list[str] = []
    for path in sorted(CACHE.glob("*.html")):
        name, kind, usage, markdown = convert(path)
        if kind == "filter":
            filters.append((name, usage, markdown))
        else:
            services.append(markdown)

    filters.sort(key=lambda f: f[0].lower())
    parts = [PREAMBLE, "", "| Filter | Usage |", "|---|---|"]
    for name, usage, _ in filters:
        cell = usage.replace("|", "\\|")
        parts.append(f"| [`{name}`](#{name.lower()}) | `{cell}` |")
    parts.append("")
    parts += [markdown for _, _, markdown in filters]
    if services:
        parts += ["# Configuration", ""] + services

    OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"{len(filters)} filters + {len(services)} config pages -> {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
