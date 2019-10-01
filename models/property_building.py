# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo import models, fields, api, _
from datetime import datetime


class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = "Inmuebles"
    _inherit = 'property.property'
    _rec_name = 'nombre'

    active = fields.Boolean(default=True)
    land_id = fields.Many2one('property.land', string='Conjunto')
    foto = fields.Binary('Foto')
    nombre = fields.Char('Nombre del inmueble')
    type_prop = fields.Many2one('building.type', string='Tipo de Inmueble')
    categ_id = fields.Many2one('property.building.categ', string="Categoria")
    room_ids = fields.One2many('property.room', 'building_id', string="Lugares")
    familia_ids = fields.One2many('property.family', 'building_id', string="Familia")
    helper_ids = fields.One2many('property.helper','building_id',string="Colaboradores")
    vehiculos_ids = fields.One2many('property.vehicle', 'building_id', string="Vehiculos")
    mascotas_ids = fields.One2many('property.pet', 'building_id', string="Mascotas")
    features_ids = fields.One2many('property.features', 'building_id', string="Features")
    administrator_id = fields.Many2one('property.property_owner', string="Propietario")
    purpose_prop = fields.Selection([('sale', 'Venta'), ('rent', 'Arriendo'),
                                  ], string="Estado de la propiedad")
    deposit = fields.Float('Deposito')
    rent_domain = fields.Selection([('family', 'Familia'), ('one_person', 'Persona Sola'),('due','Pareja')], string="Estado de la propiedad")
    rented_room = fields.Boolean('Esta arrendado?')
    tenant_id = fields.Many2one('property.property_lessee', string="Arrendatario")
    admon_value = fields.Float(string='Valor Administracion')
    dormitorios = fields.Float('Dormitorios')
    baños = fields.Float('Baños')
    balcones = fields.Float('Balcones')
    mobiliario = fields.Selection([('amoblado', 'Amoblado'),('no_amoblado','Sin amoblar')], string="Mobiliario")
    aditional_room = fields.Text('Habitaciones adicionales')
    property_services = fields.Text('Servicios Publicos')
    society_services = fields.Text('Servicios Internoss')
    note = fields.Text('Descripcion')
    can_edit_detail = fields.Boolean(compute='_compute_can_edit_detail')

    def _compute_can_edit_detail(self):
        self.can_edit_detail = self.env.user.has_group('ofimatica_property.group_property_owner')

    @api.model
    def create(self, vals):
        result = super(PropertyBuilding, self).create(vals)
        return result



class PropertyFeatures(models.Model):
    _name = 'property.features'
    _description = "Features"

    building_id = fields.Many2one('property.building', string='Building', required=True)
    categ = fields.Selection([
        ('E', 'Extinguishers'),
        ('H', 'Hydrants'),
        ('M', 'Medical kits'),
        ('A', 'Air conditioning equipment'),
        ('D', 'Deflector'),
        ('W', 'Water dispensers'),
        ('L', 'Lightning discharger'),
        ('G', 'Grounding socket '),
        ('S', 'Signage')
    ], string='Features')

    number = fields.Integer()


