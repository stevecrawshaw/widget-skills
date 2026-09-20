# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Turn the scraped ODS widget documentation into a clean reference tree.

The scrape (docs/widgets_documentation.md) is one flat 4,300-line file whose
code examples carry baked-in line numbers:

    1. <ods-chart>
      2.     <ods-chart-query context="trees">

The original indentation survives *after* the "N. " prefix, so stripping the
prefix restores the source exactly. Everything else here is regrouping: one
file per widget family, plus an index.

Run: uv run scripts/build_reference.py
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "widgets_documentation.md"
OUT = ROOT / "skill" / "reference"
OVERRIDES = ROOT / "overrides"

EXPECTED_WIDGETS = 67

# A "### heading" starts a new widget only if it names one. Every other ###
# in the scrape ("Available chart types:", "Directive info") is a subsection
# of the widget above it.
WIDGET_HEADING = re.compile(r"^### (ods[A-Z]\w*|refineOnClick)\s*$")
NUMBERED_LINE = re.compile(r"^\s*\d+\. ")

# The scrape emits every parameter list twice. The "Param| Type| Details"
# pseudo-table keeps the type boundaries intact; the Markdown table below it
# has had its links stripped in a way that ran the types together
# ("CatalogContextDatasetContextCatalogContext[]"). So rebuild from the
# pseudo-table and discard the damaged duplicate.
PSEUDO_HEADER = re.compile(r"^Param\|\s*Type\|\s*Details\s*$")
PSEUDO_RULE = re.compile(r"^-+\|-+\|-+\s*$")
# Parameter names vary wildly ("[cumulative]", "*TimeField _(optional)_",
# "[refineOnClick[context]ContextField]"), so identify a row by its shape:
# exactly two pipes. Continuation lines are prose and bullets, which have none.
PROPER_HEADER = re.compile(r"^\|\s*Parameter\s*\|\s*Type\s*\|\s*Details\s*\|$")
PROPER_RULE = re.compile(r"^\|[-\s|]+\|$")
LINK = re.compile(r"\[((?:[^\[\]]|\[\])*)\]\([^)]*\)")
# Only the empty-target ones are scrape noise; real URLs are worth keeping.
EMPTY_LINK = re.compile(r"\[((?:[^\[\]]|\[\])*)\]\(\)")

FAMILIES: dict[str, tuple[str, tuple[str, ...]]] = {
    "context": (
        "Contexts and schema",
        ("odsDatasetContext", "odsCatalogContext", "odsDatasetSchema",
         "odsPageRefresh", "odsTimer", "odsDatetime", "odsToggleModel"),
    ),
    "chart": (
        "Charts",
        ("odsChart", "odsChartQuery", "odsChartSerie", "odsLegend",
         "odsColorGradient", "odsTimescale"),
    ),
    "map": (
        "Maps and geo",
        ("odsMap", "odsMapLayer", "odsMapLayerGroup", "odsGeoNavigation",
         "odsGeotooltip"),
    ),
    "aggregation": (
        "Aggregation and analysis",
        ("odsAggregation", "odsSubaggregation", "odsAnalysis",
         "odsAdvAnalysis", "odsFacetResults", "odsDomainStatistics"),
    ),
    "filter": (
        "Filtering and search",
        ("odsFacets", "odsFilterSummary", "odsClearAllFilters", "odsSearchbox",
         "odsTextSearch", "odsSelect", "odsTimerange", "odsDateRangeSlider",
         "odsTagCloud", "refineOnClick"),
    ),
    "table": (
        "Tables and result lists",
        ("odsTable", "odsCrossTable", "odsAdvTable", "odsResults",
         "odsResultEnumerator", "odsInfiniteScrollResults",
         "odsPaginationBlock", "odsCalendar"),
    ),
    "display": (
        "Value and media display",
        ("odsGauge", "odsPicto", "odsThemePicto", "odsMediaGallery",
         "odsSlideshow", "odsRecordImage", "odsGist", "odsSocialButtons",
         "odsDisqus", "odsHubspotForm"),
    ),
    "catalog": (
        "Catalogue and portal-wide widgets",
        ("odsLastDatasetsFeed", "odsLastReusesFeed", "odsMostPopularDatasets",
         "odsMostUsedThemes", "odsThemeBoxes", "odsTopPublishers", "odsReuses"),
    ),
    "layout": (
        "Layout and page furniture",
        ("odsSimpleTab", "odsSimpleTabs", "odsPopIn", "odsSpinner",
         "odsWidgetTooltip", "odsAutoResize", "odsGetElementLayout",
         "odsGetWindowLayout"),
    ),
}


FAMILY_PREAMBLE = """\
Parameter names below are camelCase, as AngularJS normalises them internally.
In your HTML write them kebab-case: `chartType` is `chart-type=""`,
`expressionY` is `expression-y=""`, `refineOnClickContext` is
`refine-on-click-context=""`.

Check each widget's Usage block for whether it is an element (`<ods-chart>`)
or an attribute (`<div ods-aggregation="n">`). Using an attribute directive as
an element renders nothing and reports no error."""


@dataclass
class Widget:
    name: str
    lines: list[str] = field(default_factory=list)

    @property
    def body(self) -> str:
        return "\n".join(self.lines).strip()


def unmangle(lines: list[str]) -> list[str]:
    """Strip baked-in line numbers and fence the resulting code blocks."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if NUMBERED_LINE.match(lines[i]):
            block: list[str] = []
            while i < len(lines) and NUMBERED_LINE.match(lines[i]):
                # Remove the prefix and exactly one following space; the rest
                # of the leading whitespace is the example's own indentation.
                block.append(NUMBERED_LINE.sub("", lines[i], count=1).rstrip())
                i += 1
            # The scrape leaves whitespace-only filler after each block.
            while i < len(lines) and not lines[i].strip():
                i += 1
            out.extend(["```html", *block, "```", ""])
        else:
            out.append(lines[i].rstrip())
            i += 1
    return out


def _types(cell: str) -> str:
    """Adjacent `[Type]()` links are alternatives, not one run-on word."""
    links = [t.strip() for t in LINK.findall(cell) if t.strip()]
    if links:
        return " or ".join(links)
    return LINK.sub(r"\1", cell).strip()


def normalise_parameters(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        if PSEUDO_HEADER.match(stripped):
            i += 1
            if i < len(lines) and PSEUDO_RULE.match(lines[i].strip()):
                i += 1
            # Details often run over several lines (bulleted lists, a trailing
            # default), so a row ends only where the next one begins. The
            # table itself ends at the next heading or code block.
            rows: list[list[str]] = []
            while i < len(lines):
                line = lines[i]
                if line.lstrip().startswith("#") or NUMBERED_LINE.match(line):
                    break
                if line.count("|") == 2:
                    name, typ, details = line.split("|")
                    rows.append([
                        EMPTY_LINK.sub(r"\1", name).strip(),
                        _types(typ),
                        EMPTY_LINK.sub(r"\1", details).strip(),
                    ])
                elif rows and line.strip():
                    rows[-1][2] += "<br>" + EMPTY_LINK.sub(r"\1", line).strip()
                i += 1
            for row in rows:
                # The scrape wraps optional parameters in square brackets.
                # Spell that out rather than leaving it to convention.
                bracketed = re.fullmatch(r"\[(.+)\]", row[0])
                if bracketed:
                    row[0] = bracketed.group(1)
                    row[1] = f"{row[1]}, optional" if row[1] else "optional"
                details = row[2].replace("|", "\\|")
                while details.startswith("<br>"):
                    details = details[4:]
                while details.endswith("<br>"):
                    details = details[:-4]
                row[2] = details.strip()
            out += ["| Parameter | Type | Details |", "|---|---|---|"]
            out += [f"| `{n}` | {t} | {d} |" for n, t, d in rows]
            out.append("")
            continue

        if PROPER_HEADER.match(stripped):
            # Drop the duplicate, and the second "#### Parameters" above it.
            while out and (not out[-1].strip()
                           or out[-1].strip() == "#### Parameters"):
                if out.pop().strip() == "#### Parameters":
                    break
            i += 1
            if i < len(lines) and PROPER_RULE.match(lines[i].strip()):
                i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                i += 1
            continue

        out.append(lines[i])
        i += 1
    return out


def demote_stray_headings(lines: list[str]) -> list[str]:
    """`### Directive info` and friends are subsections, not widgets."""
    return [f"#{ln}" if ln.startswith("### ") else ln for ln in lines]


def collapse_blanks(lines: list[str]) -> list[str]:
    out: list[str] = []
    for ln in lines:
        if not ln.strip() and out and not out[-1].strip():
            continue
        out.append(ln)
    return out


def parse(source: str) -> list[Widget]:
    widgets: list[Widget] = []
    current: Widget | None = None
    for raw in source.splitlines():
        match = WIDGET_HEADING.match(raw)
        if match:
            current = Widget(name=match.group(1))
            widgets.append(current)
            continue
        if current is None:
            continue  # preamble before the first widget
        if raw.strip() == "---":
            continue  # scrape separator; families supply their own structure
        current.lines.append(raw)
    return widgets


def usage_form(body: str) -> str:
    """Element or attribute? Getting this wrong renders nothing, silently."""
    element = re.search(r"as element:", body, re.I)
    attribute = re.search(r"as attribute:?", body, re.I)
    if element and attribute:
        return "element or attribute"
    if element:
        return "element"
    if attribute:
        return "attribute"
    return "unknown"


def summarise(body: str) -> str:
    """First real sentence of the description, for the index."""
    match = re.search(r"#### Description\s*\n+(.+?)(?:\n\n|\Z)", body, re.S)
    if not match:
        return ""
    text = " ".join(match.group(1).split())
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # drop link targets
    sentence = re.split(r"(?<=[.])\s+", text)[0]
    return sentence.strip()


def main() -> int:
    if not SOURCE.exists():
        print(f"missing source: {SOURCE}", file=sys.stderr)
        return 1

    widgets = parse(SOURCE.read_text(encoding="utf-8"))
    by_name = {w.name: w for w in widgets}

    if len(widgets) != EXPECTED_WIDGETS:
        print(f"expected {EXPECTED_WIDGETS} widgets, parsed {len(widgets)}",
              file=sys.stderr)
        return 1

    placed = {n for _, names in FAMILIES.values() for n in names}
    if missing := sorted(set(by_name) - placed):
        print(f"widgets in no family: {missing}", file=sys.stderr)
        return 1
    if unknown := sorted(placed - set(by_name)):
        print(f"family names no such widget: {unknown}", file=sys.stderr)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    index: list[tuple[str, str, str, str]] = []

    for slug, (title, names) in FAMILIES.items():
        parts = [f"# {title}", "", FAMILY_PREAMBLE, ""]
        for name in names:
            widget = by_name[name]
            body = "\n".join(
                collapse_blanks(
                    unmangle(
                        normalise_parameters(
                            demote_stray_headings(widget.lines)
                        )
                    )
                )
            ).strip()
            override = OVERRIDES / f"{name}.md"
            if override.exists():
                body += "\n\n#### Notes\n\n" + override.read_text(
                    encoding="utf-8"
                ).strip()
            parts += [f"## {name}", "", body, ""]
            index.append((name, usage_form(body), summarise(body), slug))
        (OUT / f"widgets-{slug}.md").write_text(
            "\n".join(parts).rstrip() + "\n", encoding="utf-8"
        )

    index.sort()
    lines = [
        "# ODS widget index",
        "",
        "Every widget, with the form it takes and the family file holding its",
        "full parameters. Using an attribute directive as an element renders",
        "nothing and logs nothing, so check the Form column before writing.",
        "",
        "| Widget | Form | Purpose | Family file |",
        "|---|---|---|---|",
    ]
    for name, form, purpose, slug in index:
        purpose = purpose.replace("|", "\\|")
        lines.append(f"| `{name}` | {form} | {purpose} | `widgets-{slug}.md` |")
    (OUT / "widget-index.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )

    print(f"{len(widgets)} widgets -> {len(FAMILIES)} family files + index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
