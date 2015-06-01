import openerp.exceptions
from openerp.osv import osv
from openerp import SUPERUSER_ID

class users(osv.osv):
    _inherit = "res.users"

    def check_credentials(self, cr, uid, password):
        try:
            if uid == SUPERUSER_ID:
                super(users, self).check_credentials(cr, uid, password)
            else:
                raise openerp.exceptions.AccessDenied()
        except openerp.exceptions.AccessDenied:

            cr.execute('SELECT login FROM res_users WHERE id=%s AND active=TRUE',
                       (int(uid),))
            res = cr.fetchone()
            if res:
                ldap_obj = self.pool['res.company.ldap']
                for conf in ldap_obj.get_ldap_dicts(cr):
                    if ldap_obj.authenticate(conf, res[0], password):
                        return
            raise