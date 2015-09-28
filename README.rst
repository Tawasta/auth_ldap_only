Auth LDAP Only
--------------

Disables logins against local passwords in Odoo res_users database.

Auth LDAP Only is an extension to auth_ldap_

.. _auth_ldap: https://apps.openerp.com/apps/8.0/auth_ldap/

Features
--------

* Only allows LDAP-authorization (disables local logins)
* Admin is excluded from LDAP-authorization, and can login via local password
* Users can be excluded from LDAP-authorization from user form
