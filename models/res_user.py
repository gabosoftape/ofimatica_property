from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

from odoo.odoo.exceptions import ValidationError


class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto asociado")
    employee_id = fields.Many2one('hr.employee',
                                  string='Empleado relacionado', ondelete='restrict', auto_join=True,
                                  help='Employee-related data of the user')
    res_group_id = fields.Many2many('res.groups', 'rel_faculty_group', string="Assign Group", required=True)


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto Asociado")
    building_id = fields.Many2one('property.building', string="Inmueble asociado")

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto asociado")
    building_id = fields.Many2one('property.building', string='Inmueble asociado')
    patern_id = fields.Many2one('res.user', string="Propietario asociado")
    
#class updateResUsers(models.Model):
#    _inherit = "res.users"
#    land_id = fields.Many2one('property.land', string="Conjunto asociado")