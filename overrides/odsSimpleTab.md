A single pane inside `odsSimpleTabs`. It carries no context of its own: the
label is the tab's caption, and everything nested inside is the pane body.

By default the pane's contents are destroyed on deselection and rebuilt on
selection, which resets any widget inside it (a map recentres, a chart
refetches). Set `keep-content="true"` to keep the pane alive while hidden.
