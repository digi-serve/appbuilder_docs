---
parent: Concepts
title: Plugins
category: dev-concepts
is-category: plugin
layout: page
icon: fa-puzzle-piece
---

An AppBuilder plugin is a standalone javascript package. Plugins are added to a Tenant, and then individual user within the tenant will be able to use the plugin given they have the permission.

Plugins should be added to `/assets/`. Plugins common to all tenants (like the ABDesigner) should go into `/assets/default`. Plugins for a given tenant should be added to a folder with the tenant's id (`assets/tenants/${tenant_id}`).

Plugins need to export a function that accepts the `ABFactory` as a variable.
