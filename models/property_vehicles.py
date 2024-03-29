from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class PropertyVehicle(models.Model):
    _name = 'property.vehicle'
    _rec_name = 'placa'
    building_id = fields.Many2one('property.building', string='Inmueble', required=True)
    #foto = fields.Binary('Foto')
    propietario = fields.Char('Propietario')
    doc_propietario = fields.Char('Documento Propietario')
    tipo = fields.Selection([('bici','Bicicleta'),('moto','Moto'),('carro','Carro')],string="Tipo")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    placa = fields.Char(string="Placa")
    color = fields.Char(string="Color")
    parqueadero = fields.Char(string="Parqueadero")




