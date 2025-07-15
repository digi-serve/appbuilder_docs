---
parent: Concepts
title: Tenants
category: dev-concepts
---

A tenant is a group of users with it's own set of Apps and Data.

## Adding a Tenant

To add a tenant use the ab-cli tool used to install AppBuilder and answer the prompts.

```sh
$ appbuilder tenant add
? Tenant Key :
? Enter Tenant Name :
? What kind of authentication method:
? Enter the Tenant Administrator Username:
? Enter the Tenant Administrator password:
? Enter the Tenant Administrator email:
? Enter the port your API stack is listening on:
? Enter the LoginTenant key:
? Enter the LoginUserEmail:
? Enter the LoginPassword:
```

The tenant key will be used for the url (`key.domain.com`).

For Tenant Administrator enter the details of a new user who will be the Administrator for the new Tenant.

For the Login Tenant, Username and Password enter the details used when installing AppBuilder (the main Tenant's Administrator).

<!-- ## Removing Tenants
Remove a tenant using the ab-cli tool.
```sh
$ appbuilder tenant rm
``` -->
