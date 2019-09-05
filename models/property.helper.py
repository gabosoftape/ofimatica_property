from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class PropertyHelper(models.Model):
    _name = 'property.helper'

    building_id = fields.Many2one('property.building', string='Inmueble', required=True)
    funcion = fields.Char('Función')
    nombre = fields.Char(string="Nombres")
    apellido = fields.Char(string="Apellidos")
    doc_type = fields.Selection([('ti','Tarjeta de Identidad'),('cc','Cedula de Ciudadanía'),('ce','Cedula de Extranjeria')])
    doc_id = fields.Char('Numero de Documento')
    telefono = fields.Char('Telefono fijo')
    celular = fields.Char('Celular')
