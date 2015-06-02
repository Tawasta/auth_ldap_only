Auth LDAP Only
--------------

Auth LDAP Only is an extension to auth_ldap (https://github.com/OCA/OCB/tree/8.0/addons/auth_ldap)
Its purpose is to disable logins against passwords in Odoo res_users database.

Features
--------

* Only allows LDAP-authorization (disables local logins)
* Admin is excluded from LDAP-authorization, and can login via local password