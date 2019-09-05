from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class PropertyFamily(models.Model):
    _name = 'property.family'

    building_id = fields.Many2one('property.building', string='Inmueble', required=True)
    nombre = fields.Char(string="Nombre")
    raza = fields.Char(string="Raza")
    color = fields.Char(string="Color")
    seña = fields.Char(string="Seña Particular")
    placa = fields.Char(string="No. Placa")