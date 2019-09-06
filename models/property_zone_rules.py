from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class ZoneRules(models.Model):
    _name = 'property.rules'
    building_id = fields.Many2one('property.room', string='Zona', required=True)
    dia = fields.Selection([('lunes','Lunes'),
        ('martes','Martes'),
        ('miercoles','Miercoles'),
        ('jueves','Jueves'),
        ('viernes','Viernes'),
        ('sabado','Sábado'),
        ('domingo','Domingo')
    ],
        string="Dia", required=True)
    desde = fields.Float(string="Desde")
    hasta = fields.Float(string="Hasta")