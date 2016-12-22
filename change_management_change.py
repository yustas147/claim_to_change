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