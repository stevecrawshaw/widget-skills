---
name: ods-pages
description: Build and debug Opendatasoft (Huwise) portal pages — ods-widgets directives, AngularJS templates, page CSS, the local dev kit. Use when writing or editing a portal page's HTML/EJS or SCSS, picking a widget, wiring contexts and filters, or when a widget renders blank.
---

# Opendatasoft page development

An ODS page is HTML plus CSS, held in two tabs in the portal back office. The
HTML is an AngularJS template in which **widgets** (`ods-*` directives) fetch
data from the portal API and publish it into scope for you to bind to. You
write no JavaScript.

Assume the reader knows the Opendatasoft platform — datasets, facets, the back
office — but is not fluent in AngularJS or CSS layout.

## Silent failures

Widgets fail by rendering nothing. They do not throw, and the console stays
clean, so a blank page is the normal symptom of every mistake below. Check
these before debugging anything else.

- **Element versus attribute.** Each widget is one or the other.
  `<ods-chart>` is an element; `ods-aggregation` is an attribute on a `div`.
  Writing an attribute directive as an element renders nothing. The Form
  column in `reference/widget-index.md` says which.
- **Attribute names are kebab-case in HTML** even though the reference lists
  them camelCase: `chartType` is written `chart-type`.
- **A widget's variable is scoped to the element that declares it.**
  `ods-aggregation="n"` makes `n` available inside that element only.
- **Context parameters carry the context's name as a prefix.**
  `context="epc"` means the dataset attribute is `epc-dataset`.
- **`ods-chart` can only group by a declared facet.** Grouping on a text field
  that is not declared as a facet in the back office returns
  `Unknown facet name` from the analyze API and draws an empty chart. Use
  `ods-facet-results` instead, which goes through the search API and accepts
  any field. See `reference/recipes.md`.
- **Charts and maps need an explicit height** on a wrapper element, or they
  collapse to nothing.
- **Not every `ods-*` attribute in an existing page comes from ods-widgets.**
  `ods-tooltip` is used throughout the library's own templates but is not
  registered in `ods-widgets.js`, so it works on the portal and does nothing
  in a local kit or the preview harness. Before copying an attribute out of a
  live page, check it is in the index; if it is not, expect it to be inert
  locally and verify on the portal.

## Steps

### 1. Find the environment

Look for a local dev kit (a repo with `pages/views/*.ejs`, `pages/styles/*.scss`
and `config.project.js`). If there is one, read its `CLAUDE.md` and `README.md`
first: they hold the portal domain, the build and publish commands, and the
gotchas specific to that portal. Those files are authoritative where they
disagree with anything here.

With no local kit, write the HTML and CSS as two separate blocks for the user
to paste into the back office.

### 2. Confirm the data before writing markup

Never assume a field name or that a facet exists. Ask the API:

```
https://<portal>/api/explore/v2.1/catalog/datasets/<dataset>            # fields
https://<portal>/api/explore/v2.1/catalog/datasets/<dataset>/facets     # facets
https://<portal>/api/explore/v2.1/catalog/datasets/<dataset>/records?limit=3
```

Done when you have the exact field names, their types, and the list of
declared facets in hand. Most blank pages trace back to skipping this.

### 3. Choose the widgets

Read `reference/widget-index.md` in full — it is short, and it is the only
file that maps a need to a widget. Then open **one** family file, the one the
index points at. Do not read the other eight: they are 200 to 550 lines each
and hold unrelated widgets.

Family files group widgets that must be used together, so a chart task gets
`odsChart`, `odsChartQuery` and `odsChartSerie` in one read.

Load `reference/filters-and-config.md` only for a binding filter, a date or
number format, or a portal config value such as basemaps or chart colours.

### 4. Write the page

Start from the nearest fragment in `reference/recipes.md` rather than from
scratch, and check whether it is marked tested.

Load `reference/angularjs-in-ods.md` when a binding misbehaves or you are
unsure how a widget's variable reaches the template — it covers the ODS
specifics, not AngularJS generally. Load `reference/css-and-layout.md` when
laying out more than one element, or when a chart or map needs sizing.

### 5. Verify that it renders real values

Build, serve, and render the page, then confirm the expected values are in the
DOM — not merely that the build passed.

```bash
google-chrome --headless=new --dump-dom --virtual-time-budget=30000 <url>
```

With no dev kit, or to check one widget in isolation, copy
`reference/preview-harness.html`, fill in the portal and dataset, and render
that file directly. It loads the widget library from the CDN and queries the
live portal from a `file://` URL.

Wrap values in sentinels (`RATING:{{ r.name }}:END`) so you can grep them out
of the dumped DOM.

Done when every figure, label and list you added appears in the dumped DOM
with real data in it. An empty element that should hold a number means the
page is broken, however clean the build was.

Headless Chrome does not wait for the chart library's lazily-loaded modules,
so a chart shows only its loading spinner even when correct. Confirm a chart
by running its query instead:

```
<portal>/api/records/1.0/analyze/?dataset=<dataset>&x=<field>&y.count.func=COUNT
```

Then ask the user to look at the chart in a real browser, saying plainly that
is what remains unverified.

### 6. Hand over for publishing

Publishing is a manual paste into the back office unless the project's own
docs say otherwise: `output/<slug>.html` into the HTML tab,
`output/<slug>.css` into the CSS tab. Tell the user to keep a copy of the live
page first, because the portal has no undo.

## Reference

| File | Holds |
|---|---|
| `reference/widget-index.md` | All 67 widgets: form, purpose, which family file |
| `reference/widgets-<family>.md` | Full parameters and examples, nine families |
| `reference/filters-and-config.md` | The 34 ods-widgets filters, AngularJS built-ins, `ODSWidgetsConfig` |
| `reference/angularjs-in-ods.md` | The AngularJS subset ODS pages use |
| `reference/css-and-layout.md` | Bootstrap 3 grid, sizing, SCSS in the kit |
| `reference/recipes.md` | Working page fragments, marked tested or untested |
| `reference/preview-harness.html` | Standalone page for checking widgets against a live portal |

The online code library at <https://codelibrary.opendatasoft.com/> has fuller
worked examples — page templates, components, widget tricks — and is worth
pointing the user at when they want to browse for ideas.
