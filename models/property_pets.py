from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class PropertyPet (models.Model):
    _name = 'property.pet'
    building_id = fields.Many2one('property.building', string='Inmueble', required=True)
    foto_placa = fields.Binary('Foto Placa')
    foto = fields.Binary('Foto Animal')
    tipo = fields.Char(string="Tipo")
    raza = fields.Char(string="Raza")
    nombre = fields.Char(string="Nombre")
    color = fields.Char(string="Color")