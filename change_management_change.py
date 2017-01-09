# coding: utf-8

from openerp.osv import fields, osv



class change_management_change(osv.osv):
    """Convert Claim to Change Wizard"""

    _name = 'change.management.change'
    _inherit = 'change.management.change'

    _columns = {
        "claim_id": fields.many2one(
             "crm.claim", "Claim"
        ),
    }    

class crm_claim(osv.osv):
    _name = 'crm.claim'
    _inherit = 'crm.claim'

    _columns = {
        "change_ids": fields.one2many('change.management.change', 'claim_id', string='Child Changes', 
                                     limit=None, 
                                     auto_join=False),
    }    


