# ods-pages skill

Source for the `ods-pages` Claude Code skill: building pages for Opendatasoft
(Huwise) portals with ods-widgets, AngularJS templates and CSS.

Installed globally by symlink, so edits here take effect immediately:

```bash
ln -sfn "$PWD/skill" ~/.claude/skills/ods-pages
```

## Layout

| Path | Purpose | Edit by hand? |
|---|---|---|
| `skill/SKILL.md` | The skill itself | Yes |
| `skill/reference/angularjs-in-ods.md` | AngularJS subset ODS pages use | Yes |
| `skill/reference/css-and-layout.md` | Grid, sizing, SCSS | Yes |
| `skill/reference/recipes.md` | Page fragments, marked tested or untested | Yes |
| `skill/reference/preview-harness.html` | Standalone widget test page | Yes |
| `skill/reference/widget-index.md` | Generated | No |
| `skill/reference/widgets-*.md` | Generated, nine families | No |
| `skill/reference/filters-and-config.md` | Generated | No |
| `overrides/<widget>.md` | Hand-written notes merged into a widget's entry | Yes |
| `docs/widgets_documentation.md` | Scraped widget docs, the build input | No |
| `partials/` | Cached ngdocs pages for filters and config | No |

## Rebuilding the generated reference

```bash
uv run scripts/build_reference.py           # widgets, from docs/
uv run scripts/build_filters.py             # filters, from partials/
uv run scripts/build_filters.py --fetch     # refresh partials from the web first
```

`build_reference.py` repairs the scrape: it strips the line numbers baked into
every code example, fences them, rebuilds the parameter tables from the
pseudo-table (the scrape's Markdown copy has run-together types), marks
optional parameters, and splits 67 widgets into nine family files. It fails
loudly if the widget count changes or a widget belongs to no family.

To correct or extend a generated widget entry, add `overrides/<widgetName>.md`.
It is appended under a Notes heading and survives rebuilds — never edit the
generated files, as the next build discards the change.

## Sources

- Widget directives: `docs/widgets_documentation.md`, a scrape of
  <https://help.opendatasoft.com/widgets/#/api/>
- Filters and config: the same site's ngdocs partials, which the scrape missed
- Worked examples for humans: <https://codelibrary.opendatasoft.com/>
