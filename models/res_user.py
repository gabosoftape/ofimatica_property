from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

    @api.model_create_multi
    def create(self, vals):
        voucher_user = self.env['res.users'].create({
            'name': self.name,
            'login': self.login,
            'email': self.login,
            'company_id': self.env.ref('base.main_company').id,
            'groups_id': [(6, 0, [
                self.ref('group_property_admin')
            ])]
        })
        return voucher_user


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')