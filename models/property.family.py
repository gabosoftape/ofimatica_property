from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class PropertyFamily(models.Model):
    _name = 'property.family'

    building_id = fields.Many2one('property.building', string='Inmueble', required=True)
    parentezco = fields.Char('Parentezco')
    nombre = fields.Char('Nombres')
    apellidos = fields.Char('Apellidos')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')
    emergency_name = fields.Char('En caso de emergencia llamar a')
    emergency_tel = fields.Char('Telefono')