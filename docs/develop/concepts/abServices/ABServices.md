---
title: AppBuilder Services
category: dev-concepts
layout: page
parent: Concepts
---

As of version 2, AppBuilder is deployed as a docker swarm with the following services:

## Third Party Services

### `mariadb`

We use Maria DB as our backend database.

**image:** [mariadb](https://hub.docker.com/_/mariadb/)

### `redis`

We use redis to allow cote services to find each other across the swarm

**image:** [redis](https://hub.docker.com/_/redis/)

## AppBuilder Services

### `config`

Simply exists to pull in the config/local.js into our config volume

**repo:** [ab_service_config](https://github.com/CruGlobal/ab_service_config)

### `api_sails`

Our API end point

**repo:** [ab_service_api_sails](https://github.com/CruGlobal/ab_service_api_sails)

### `appbuilder`

(AppBuilder) A multi-tenant aware service to process our AppBuilder requests.

**repo:** [ab_service_appbuilder](https://github.com/CruGlobal/ab_service_appbuilder)\
&nbsp;↳ **sub:** [appbuilder_platform_service](https://github.com/CruGlobal/appbuilder_platform_service)\
&nbsp;&nbsp;&nbsp;&nbsp;↳ **sub:** [appbuilder_class_core](https://github.com/CruGlobal/appbuilder_class_core)

### `bot_manager`

Our #slack bot service

**repo:** [ab_service_bot_manager](https://github.com/CruGlobal/ab_service_bot_manager)

### `definition_manager`

A service to manage the definitions for a running AppBuilder

**repo:** [ab_service_definition_manager](https://github.com/CruGlobal/ab_service_definition_manager)\
&nbsp;↳ **sub:** [appbuilder_platform_service](https://github.com/CruGlobal/appbuilder_platform_service)\
&nbsp;&nbsp;&nbsp;&nbsp;↳ **sub:** [appbuilder_class_core](https://github.com/CruGlobal/appbuilder_class_core)

### `file_processor`

A service to manage uploaded files.

**repo:** [ab_service_file_processor](https://github.com/CruGlobal/ab_service_file_processor)\
&nbsp;↳ **sub:** [appbuilder_platform_service](https://github.com/CruGlobal/appbuilder_platform_service)\
&nbsp;&nbsp;&nbsp;&nbsp;↳ **sub:** [appbuilder_class_core](https://github.com/CruGlobal/appbuilder_class_core)

### `log_manager`

A log manager for various AppBuilder operations

**repo:** [ab_service_log_manager](https://github.com/CruGlobal/ab_service_log_manager)

### `notification_email`

An smtp email service

**repo:** [ab_service_notification_email](https://github.com/appdevdesigns/ab_service_notification_email)

### `process_manager`

A micro service to manage our process tasks

**repo:** [ab_service_process_manager](https://github.com/CruGlobal/ab_service_process_manager)\
&nbsp;↳ **sub:** [appbuilder_platform_service](https://github.com/CruGlobal/appbuilder_platform_service)\
&nbsp;&nbsp;&nbsp;&nbsp;↳ **sub:** [appbuilder_class_core](https://github.com/CruGlobal/appbuilder_class_core)

### `tenant_manager`

A service to manage the site's tenants

**repo:** [ab_service_tenant_manager](https://github.com/CruGlobal/ab_service_tenant_manager)

### `user_manager`

A microservice for managing Users

**repo:** [ab_service_user_manager](https://github.com/CruGlobal/ab_service_user_manager)\
&nbsp;↳ **sub:** [appbuilder_platform_service](https://github.com/CruGlobal/appbuilder_platform_service)\
&nbsp;&nbsp;&nbsp;&nbsp;↳ **sub:** [appbuilder_class_core](https://github.com/CruGlobal/appbuilder_class_core)
