The parameters listed above (`name`, `title`, `sort`, `visibleItems`,
`disjunctive`, `hideIfSingleCategory`) go on the **`<ods-facet>` children**,
not on `<ods-facets>` itself. The parent takes only `context`.

`odsFacet` is a real directive in the widget library but has no page of its
own in the documentation, which is why it appears nowhere in the index.

```html
<ods-facets context="epc">
    <ods-facet name="current_energy_rating" title="Rating"></ods-facet>
    <ods-facet name="local_authority_label" title="Authority"
               visible-items="5" sort="-count"></ods-facet>
</ods-facets>
```

Each `name` must be a field **declared as a facet** on the dataset. An
undeclared field renders an empty filter with its title and nothing beneath.
