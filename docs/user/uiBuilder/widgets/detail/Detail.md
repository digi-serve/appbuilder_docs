---
parent: User Interface Designer
parent: widgets
category: widgets
title: Detail
layout: page
---
Displays the details of one record in a given data collection. Any page with a detail widget can be used as a linked detail page from certain widgets (given they use the same data collection).

## Internal Widgets

After selecting the data source a widget is added for each field in the data collection. These can be removed. Using the edit button you can adjust height for the individual field. Depending on the field type other properties are available. In most cases editing the individual field widgets is unnecessary.

You can also add [label](../label/Label.md) and [text](../text/Text.md) widgets to customize the look of the detail.

## Properties

**Columns** - Adjusts the number of columns.

**Column Gravity** - Adjust the column width relative to the other columns.

**Data Source** - Select the data collection to use.\
After selecting the data source a list of fields from data collection is listed. Unselect to hide any field.

**Display Label** - Unselect to hide the field names, leaving just the values.

**Label Position** - Choose to place the label Left or Above the values.

**Label Width** - Adjust the space for the label text. Labels longer than the label width are cut off.

**Height** - Set the widget height. With Height set to 0 the widget will scale automatically based on the contents.

## Troubleshoot

### No values are displayed

If you see only labels with no values this means that there is no selection made on the data collection. Set a selection on the data collection. [add a link]
