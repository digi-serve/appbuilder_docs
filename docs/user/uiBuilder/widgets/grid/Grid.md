---
parent: User Interface Designer
category: widgets
title: Grid
---

Display a table with a multiple records.

## Properties

### Grid Properties

**User can edit in grid** - Select to allow user to click and edit records in the grid.

**User can edit multiple items at one time** - Displays an **Edit** button above the grid and checkboxes next to each record. Users can select records with the checkboxes and then use the **Edit** button to set selected fields to the same value.

**User can delete records** - Displays a delete icon next to each record, allowing user to delete records. The deleted records will be permanently removed, so think through whether this setting is needed.

**User can sort records** - Displays an **Apply Sort** button above the grid. User can click to sort by the fields they choose.

**User can export** - Displays an **Export** Button above the grid. Users can download the grid contents as CSV, Excel, PDF or PNG.\
_Note: Only the loaded data will be exported. By default this is the first 30 records. Using the load all option on your data collection will allow user to export the full data set; however, load all on large data set will slow down page loading. For large data exports use the [CSV Exporter](../csvExporter/CsvExporter.md)._

### Grid Data

**Object** - Select the data collection to display in the grid.

### Group

Records can be grouped by a common field. A summary line of the group will show the total for number fields and count for other fields. User can click to expand the group and see each record as they normally would.

**Group by** - Choose which fields to group records by.\
After adding the fields drag and drop in the space below to reorder the grouping hierarchy.

### Linked Pages

**Details Page** - Select to link a detail page. Valid pages, containing a detail widget using the same data collection, are listed. Users see an eye icon next to each record.

**Edit Form** - Select to link an edit form. Valid pages, containing a form widget using the same data collection, are listed. Users see an edit icon next to each record.

### Customize Display

**Hidden Fields** - Select fields to hide from the grid.

**Filter Option** - Change whether user can use a filter and which of the [filter](../../../concepts/filters/Filters.md) variants to use.

- Do not Allow User filters - Don't show any filter options
- Enable User filters - User can click to add multiple filters.
- Toolbar - Displays an **Add filters** button in the toolbar above the grid. Filters are added in a popup.
- Form - Displays an **Add filters** button above the grid. Filters added display above the grid.
- Include a global filter input - with the toolbar selection this option adds a search bar to the toolbar.
- Use a filter menu - Displays a menu of predefined filters for the user to choose from.
- Use a global filter input - Displays a search bar. Search for records contain the text in any field.\
  _Note: Does not filter based on labels of connected records or select lists. Connected records using a custom index can be searched._
  > TODO: What does 'All matching records' vs 'Single records only' do

**Freeze Columns** - Choose to freeze certain columns on the left of the table. When the user scrolls horizontally the frozen fields do not scroll. All fields to the left of the selected field will be frozen. You can drag and drop in the grid to reorder the columns before freezing them.

**Summary Fields** - Select any number fields to display a total at the bottom of the grid.
_Note: This is a total of loaded records, so will be misleading on large data collection when not using load all._

**Count Fields** - Select a field to display its count at the bottom of the grid.
_Note: This is a total of loaded records, so will be misleading on large data collection when not using load all._

**Height** - adjust the grid height.

**Hide table header** - Select to hide the header.

**Show a field using label template** - Select to add a column called label to the grid. The value for each record is based on the label template set using the **Define label** button in the Object Builder.

**Hide edit and view buttons** - Select to hide the edit and view icons for linked pages. Users can still navigate to the form or detail by clicking the record.\
_Note: If both edit and detail pages are linked, only the detail page will be accessible. If using the **User can edit in grid** option neither linked page will be accessible._
