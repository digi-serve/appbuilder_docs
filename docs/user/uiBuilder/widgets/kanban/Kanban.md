---
parent: User Interface Designer
category: widgets
title: Kanban
layout: page
---

Display a kanban board with columns and cards. Kanban is a project management system. [Learn more about Kanban](https://blog.trello.com/kanban-101).

The Kanban cards display the label set using define label function in the object builder.

## Properties

### Kanban Data

**Data Source** - Select the data collection to use in the Kanban

**Vertical Grouping** - Select the field to use as the columns. This should be a select list field. Each option of the select list is a column.\
_For example use a 'Status' select list with options, 'To Do', 'In Progress', 'Done'. User will be able to drag cards between columns to update the status field_

**Horizontal Grouping** - Optionally cards can be grouped within each column based on another select list or connected record field.

**Card Owner** - Select a user field type to display on the cards. Connect record fields can also be used.

### Linked Pages

**Details Page** - Select to link a detail page. Valid pages, containing a detail widget using the same data collection, are listed.

**Edit Form** - Select to link an edit form. Valid pages, containing a form widget using the same data collection, are listed.
