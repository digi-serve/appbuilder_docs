---
title: Adding Tenant
category: admin
---

## To create a new Tenant: 

### on running system:

you are going to need to SSH into the server, and have our password manager open.
from PW manager: get the Admin Tenant credentials.

Needed information
key: bobsburgers
full name: Bobs Burgers
pw manager credentials: ~
port: while SSHed in run```docker service ls``` and look for the XXX_web service. It'll be the source under PORTS: ex ```<this number> -> <not this number>```

### cli creating steps:

1. ssh into the server then run:```$ appbuilder tenant add --authType=login```

1. key: unique "key" for the new Tenant.  This is what would be in the url:  [key].cars.org
bobsburgers

1. name: Actual long text for the Tenant name. 
Bobs Burgers

1. Tenant Admin Username: the new Tenant's admin username (usually admin) 

1. Tenant Admin Password: the new Tenant's admin password <use from PW manager>

1. Tenant Admin Email: the new Tenant's admin email

1. port: the port our current stack is listening on

To find this value: run ```docker service ls``` and look for the XXX_web service. It'll be the source under PORTS: ex ```<this number> -> <not this number>```

// this is the super admin, that works for the client to add new users etc. (this)

1. LoginTenant key: The key for our Admin Tenant (usually admin) 

1. LoginUserEmail: The email of our Admin Tenant email <use from PW manager>

1. LoginPassword: The password of our Admin Tenant

### Steps to add

1. Answer the cli questions about the new tenant admin  and the existing Tenant Admin login info.
1. open browser & log out of the existing AB portal
1. Refresh browser
1. login as the new tenant (be sure to choose the new tenant key in the droplist)
1. Add System Admin to Role(Builders)
1. To add an application:
1. Open ABDesigner and Upload the app_CARS.json definitions.

-- For Officially tested version: get the definitions from https://github.com/CruGlobal/cars_app/blob/master/test_import/module.json

## add users

As normal, under site administration