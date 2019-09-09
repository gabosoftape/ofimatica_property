from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

    def __init__(self):
        group_admin = self.env.ref('ofimatica_property.group_property_admin')
        groups_id = [(6, 0, [group_admin.id])]
        return groups_id


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')