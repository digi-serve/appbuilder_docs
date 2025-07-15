---
title: Record Rules
category: user
parent: Concepts
---
Record rules can be added to [forms](../../uiBuilder/widgets/form/Form.md) to change data after the form is submitted. They can also be applied to records imported using the [CSV Importer](../../uiBuilder/widgets/csvImporter/CsvImporter.md).

## Action

After adding a new rule an action must be selected.

**Update Record** - This action allows you to change values on the current record (submitted in the form).\
**Insert Connected Object** - This action creates a record that is connected to the form record. After selecting this action choose the connected record field to insert. Then values for the new record can set.\
**Update Connected Record** - This action changes or sets values on a connected record (that already exists). After selecting this actions choose the connected record field to update. Then set which values to update on the connected record.\
**Remove Connected Record** - This action can remove a connected record from the submitted record. This removes the connection only, the record will not be deleted.

## Values

In the values section configure which fields should be changes and how. The Action determines which record the values will modify.

Beside **Set** choose the field to update. Beside **To** set the value.

You can click **Or exists value** to use a value from existing data. To access other fields from the submitted record select the data collection used in the form, the field, and then **Current selection.**

Multiple values can be set using the same record rules.

## Custom Conditions

Custom Conditions can be added so that only records that match your condition get changed. [Filters](../filters/Filters.md) are used to set conditions.
