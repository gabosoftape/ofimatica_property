from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

    @api.model
    def create(self, vals):
        """This code is to create an employee while creating an user."""
        result = super(beehivePartner, self).create(vals)
        group_admin = self.env.ref('ofimatica_property.group_property_admin')
        result['groups_id'] = group_admin
        result['uid'] = self.id
        return result


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')