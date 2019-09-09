from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    employee_id = fields.Many2one('hr.employee',
                                  string='Administrador relacionado', ondelete='restrict', auto_join=True,
                                  help='New Client-related data of the user')

    @api.model
    def create(self, vals):
        """This code is to create an employee while creating an user."""
        result = super(beehivePartner, self).create(vals)
        group_admin = self.env.ref('ofimatica_property.group_property_admin')
        result['employee_id'] = self.env['hr.employee'].sudo().create({'name': result['name'],
                                                                       'user_id': result['id'],
                                                                       'address_home_id': result['partner_id'].id})
        result['groups_id'] = [(6, 0, [group_admin.id])]
        return result


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')