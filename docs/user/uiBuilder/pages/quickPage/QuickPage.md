---
parent: Pages
category: ui
title: Quick Page
---
# Quick Page

The quick page feature creates a set of linked pages, with preconfigured widgets. This is best used to create a grid with linked detail and edit page.

To add a quick page from **Interface** select **Add a new page** then **Quick Page**, fill in the settings and click **Add**.

## Options

**Parent Page** - Select the page to add you quick page below. Selecting `[Root Page]` makes a root page that will be displayed in the top toolbar.

**Select a data collection** - choose the main data collection to use for your quick page.

**Page Name** - By default the data collection name is used.

_These checkboxes determine what is added in your quick page. The **{data}** referenced below will appear as your data collection name._

**Display {data} into a Tab** - Select this if you wish the quick page to be a tab rather than a stand alone page. It will add a tab to a [tab widget](../../widgets/tab/Tab.md) on the parent page selected.

**Display multiple {data} in a Grid** - Select to add a [grid widget](../../widgets/grid/Grid.md) to the quick page with you selected data collection as the source.

**A Menu button linked to a page to Add a new {data}** - Select to add a [menu widget](../../widgets/menu/Menu.md) linked to a generated pop up page with a [form widget](../../widgets/form/Form.md). The form will be configured to add a new record to your data collection.

**Add a new {data} with a Form** - Select to a add a [form widget](../../widgets/form/Form.md) on the quick page configured to add a new record to your data collection.

_Selecting the following options will create a pop up page linked to the grid._

**Edit Selected {data}** - Select to add and link an edit form to the Grid.

**View details of {data}** - Select to add and link a detail page to the Grid.
