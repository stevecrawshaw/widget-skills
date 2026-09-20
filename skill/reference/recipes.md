# Page recipes

Complete fragments to start from. Each states what the dataset must provide.

**Tested** means the pattern has been rendered against a live portal and the
expected values confirmed in the DOM. **Untested** means it is assembled from
the reference and has not been run; verify it with `preview-harness.html`
before trusting it.

## Count of records (tested)

Needs: any dataset.

```html
<div ods-dataset-context
     context="epc"
     epc-dataset="epc_domestic_lep_ods">
    <div ods-aggregation="n"
         ods-aggregation-context="epc"
         ods-aggregation-function="COUNT">
        <p class="epc-kpi">{{ n | number }} certificates</p>
    </div>
</div>
```

`ods-aggregation` is an attribute, and `n` is visible only inside the element
that declares it.

## Breakdown of a text field, without declared facets (tested)

Needs: any text field. This is the reliable way to group by a text field,
because it uses the search API, which accepts a facet name ad hoc.

```html
<ul class="epc-bars"
    ods-facet-results="ratings"
    ods-facet-results-context="epc"
    ods-facet-results-facet-name="current_energy_rating"
    ods-facet-results-sort="alphanum">
    <li ng-repeat="r in ratings">
        <span class="epc-bars__label">{{ r.name }}</span>
        <span class="epc-bars__bar"
              ng-style="{ width: (r.count / n * 100) + '%' }"></span>
        <span class="epc-bars__value">{{ r.count | number }}</span>
    </li>
</ul>
```

Each item has `name`, `count` and `path`. Styles are in `css-and-layout.md`.

## Bar chart of a text field (query tested, drawing unconfirmed)

Needs: the field **declared as a facet** on the dataset, in the back office.

This is the trap that sends people to the recipe above. `ods-chart` groups
through the analyze API, which only accepts declared facets. Without the
declaration the API returns `Unknown facet name` and the chart renders as an
empty box with a timezone footer underneath — no error in the console.

```html
<div class="chart-panel">
    <ods-chart>
        <ods-chart-query context="epc"
                         field-x="current_energy_rating"
                         maxpoints="10">
            <ods-chart-serie chart-type="column"
                             function-y="COUNT"
                             expression-y="current_energy_rating"
                             color="#40A832">
            </ods-chart-serie>
        </ods-chart-query>
    </ods-chart>
</div>
```

Before writing this, confirm the facet exists. Either list the declared
facets, or run the chart's own query:

```
https://<portal>/api/explore/v2.1/catalog/datasets/<dataset>/facets
https://<portal>/api/records/1.0/analyze/?dataset=<dataset>&x=<field>&y.count.func=COUNT
```

A declared field returns `[{"x": "A", "count": 4848}, ...]`. An undeclared one
returns `{"error": "Unknown facet name '<field>'"}`, and that is exactly what
turns the chart into an empty box.

A chart needs a height on its wrapper or it collapses.

## Time series (untested)

Needs: a date or datetime field.

```html
<ods-chart>
    <ods-chart-query context="epc"
                     field-x="lodgement_date"
                     timescale="month">
        <ods-chart-serie chart-type="line"
                         function-y="COUNT"
                         expression-y="lodgement_date"
                         color="#40A832">
        </ods-chart-serie>
    </ods-chart-query>
</ods-chart>
```

`timescale` is one of `year`, `month`, `week`, `day`, `hour`, `minute`. The
date field must be declared as a facet, as for any other chart grouping.

## Filters beside a result list (tested)

Needs: the filtered fields declared as facets.

```html
<div class="container"
     ods-dataset-context
     context="epc"
     epc-dataset="epc_domestic_lep_ods">
    <div class="row">
        <div class="col-md-3">
            <ods-facets context="epc">
                <ods-facet name="current_energy_rating" title="Rating"></ods-facet>
                <ods-facet name="local_authority_label" title="Authority"></ods-facet>
            </ods-facets>
            <ods-clear-all-filters context="epc"></ods-clear-all-filters>
        </div>
        <div class="col-md-9">
            <ods-filter-summary context="epc"></ods-filter-summary>
            <ods-table context="epc"></ods-table>
        </div>
    </div>
</div>
```

Every widget sharing `context="epc"` reacts to the filters automatically;
there is nothing to wire up.

## Free-text search (tested)

```html
<ods-text-search context="epc"
                 placeholder="Search addresses">
</ods-text-search>
```

## Map of geographic records (untested)

Needs: a geo point or geo shape field.

```html
<div class="map-panel">
    <ods-map context="epc"
             location="12,51.45,-2.59"
             basemap="jawg.streets">
    </ods-map>
</div>
```

`location` is `zoom,latitude,longitude`. Give `.map-panel` an explicit height.
Omit `location` to let the map fit the data.

## Two datasets on one page (untested)

```html
<div ods-dataset-context
     context="epc,pop"
     epc-dataset="epc_domestic_lep_ods"
     pop-dataset="population_estimates">
    ...
</div>
```

Each context's settings carry its own prefix. Widgets name the one they want
with `context="epc"` or `context="pop"`.

## Debugging a blank binding

Drop this beside anything that is not appearing:

```html
<pre>{{ ratings | json }}</pre>
```

If it prints `undefined`, the variable name or its scope is wrong. If it
prints an empty array, the query ran and matched nothing, so look at the
field name, the facet declaration, or an active filter.
