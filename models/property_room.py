# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

selection_level = [('p', 'P'), ('m', 'M'), ('s', 'S')] + [(num, str(num)) for num in range(1, 30)]


class PropertyRoom(models.Model):
    _name = 'property.room'
    _description = "Zonas Comunes"

    nombre = fields.Char(string="Nombre")
    building_id = fields.Many2one('property.land', string='Cliente', required=True)
    usage = fields.Selection([
        ('office', 'Office'),
        ('meeting', 'Meeting room'),
        ('kitchens', 'Kitchens'),
        ('laboratory','Laboratory'),
        ('garage','Garage'),
        ('archive', 'Archive'),
        ('warehouse', 'Warehouse'),
        ('log_warehouse', 'Logistics warehouse'),
        ('it_endowments', 'IT endowments (Ranks, Hall Servers)'),
        ('premises', 'Technical premises (thermal, air conditioning, post-transformer)'),
        ('cloakroom', 'Cloakroom'),
        ('sanitary', 'Sanitary group'),
        ('access', 'Access ways'),
        ('lobby', 'Lobby'),
        ('staircase', 'Staircase'),
    ], string="Room usage", help="The purpose of using the room")
    last_maintenance = fields.Date()
    technical_condition = fields.Selection([(0,'Missing'),(1,'Unsatisfactory'),(3,'good'),(5,'very good')],
                                           group_operator='avg')
    foto = fields.Binary()
    valor_hora = fields.Float('Valor Hora')
    descripcion_uso = fields.Text('Descripcion de Uso')
    is_reserved = fields.Boolean('Esta reservado?')
    max_person = fields.Float('Numero permitido de personas Uso')
    is_autoreserved = fields.Boolean('esta autoreservado?')
    horario_ids = fields.One2many('property.rules', 'building_id', string="Familia")





