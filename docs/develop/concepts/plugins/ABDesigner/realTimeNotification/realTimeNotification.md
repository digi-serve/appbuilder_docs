---
parent: Concepts
title: ABDesigner Real Time Notifications
category: plugin
---

## Overview

New in our ABDesigner is our attempt at synchronizing definition changes across a Tenant's ABDesigner instances.

When a RT Notification for a changed defintion happens, the Network resource will pick it up and then emit it across the `ABFactory` object.

`ABFactory` listens for the "ab.definition.xxx" message, updates it's current list of defintions, then turns around and:

1. For objects the `ABFactory` directly manages ("object", "query", "datacollection", "process", "application") it emits the `object.emit("definition.xxxx", json)` message. Any Resource using that Object, needs to listen for that, and respond by requesting a new instance of that object from the `ABFactory`.
1. For other objects not directly managed by `ABFactory`, it emits an `AB.emit("definition.xxx", json)` message. Those objects need to listen for that message, and if the `json.id == this.id`, then personally `this.emit("definition.xxx",json)`;

## Example

If an `ABField` definition was updated.

```
io.socket emits "ab.definition.updated" --> ABFactory.Network
ABFactory.Network -> ABFactory.emit("ab.definition.updated", data);
ABFactory updates it's current definition.
ABFactory.emit("definition.updated", newDefinition);
ABField listens on "definition.updated" and finds newDefinition.id == this.id
ABField.emit("definition.updated", newDefinition);
ABObject listens on ABField for "definition.updated"
ABObject replaces current ABField with a new instance based upon the ABFactory defintions
```
