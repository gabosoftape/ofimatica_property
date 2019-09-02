# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

from odoo import models, fields, api, _
from datetime import datetime


class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = "Building"
    _inherit = 'property.property'

    land_id = fields.Many2one('property.land', string='Conjunto')
    foto = fields.Binary()
    type_prop = fields.Selection([('apto', 'Apartamento'), ('casa', 'Casa'),
                                  ('park','Parqueadero'),('study','Apartaestudio')], string="Tipo de Propiedad")
    categ_id = fields.Many2one('property.building.categ', string="Categoria")
    room_ids = fields.One2many('property.room', 'building_id', string="Lugares")
    vehiculos_ids = fields.One2many('property.vehicle', 'building_id', string="Vehiculos")
    mascotas_ids = fields.One2many('property.pet', 'building_id', string="Mascotas")
    features_ids = fields.One2many('property.features', 'building_id', string="Features")

    administrator_id = fields.Many2one('res.partner', string="Propietario", domain=[('is_company', '=', False)])

    purpose_prop = fields.Selection([('sale', 'Venta'), ('rent', 'Arriendo'),
                                  ], string="Estado de la propiedad")

    deposit = fields.Float('Deposito')
    rent_domain = fields.Selection([('family', 'Familia'), ('one_person', 'Persona Sola'),('due','Pareja')], string="Estado de la propiedad")
    rented_room = fields.Boolean()
    tenant_id = fields.Many2one('res.partner', string="Arrendatario")
    admon_value = fields.Float(string='Valor Administracion')
    dormitorios = fields.Float('Dormitorios')
    baños = fields.Float('Baños')
    balcones = fields.Float('Balcones')
    mobiliario = fields.Selection([('amoblado', 'Amoblado'),('no_amoblado','Sin amoblar')], string="Mobiliario")
    aditional_room = fields.Text('Habitaciones adicionales')
    property_services = fields.Text('Servicios Publicos')
    society_services = fields.Text('Servicios Internoss')
    name = fields.Char(string="Nombre de Inmueble")

    @api.onchange('purpose_parent_id')
    def onchange_purpose_parent_id(self):
        if self.purpose_id.parent_id != self.purpose_parent_id:
            self.purpose_id = False

        if self.purpose_parent_id:
            return {'domain': {'purpose_id': [('parent_id', '=', self.purpose_parent_id.id)]}}
        else:
            return {'domain': {'purpose_id': []}}

    @api.onchange('purpose_id')
    def onchange_purpose_id(self):
        self.purpose_parent_id = self.purpose_id.parent_id

    @api.depends('room_ids.surface_cleaning_floor', 'room_ids.floor_type')
    def _cleaning_floor(self):
        surface_cleaning_carpet = 0.0
        surface_cleaning_linoleum = 0.0
        surface_cleaning_wood = 0.0

        for room in self.room_ids:
            if room.floor_type == 'c':
                surface_cleaning_carpet += room.surface_cleaning_floor
            if room.floor_type == 'l':
                surface_cleaning_linoleum += room.surface_cleaning_floor
            if room.floor_type == 'w':
                surface_cleaning_wood += room.surface_cleaning_floor

        self.surface_cleaning_carpet = surface_cleaning_carpet
        self.surface_cleaning_linoleum = surface_cleaning_linoleum
        self.surface_cleaning_wood = surface_cleaning_wood

    @api.depends('room_ids.surface_cleaning_windows')
    def _cleaning_windows(self):
        surface_cleaning_windows = 0.0
        for room in self.room_ids:
            surface_cleaning_windows += room.surface_cleaning_windows
        self.surface_cleaning_windows = surface_cleaning_windows

    @api.depends('room_ids.surface_cleaning_doors')
    def _cleaning_doors(self):
        surface_cleaning_doors = 0.0
        for room in self.room_ids:
            surface_cleaning_doors += room.surface_cleaning_doors
        self.surface_cleaning_doors = surface_cleaning_doors

    @api.depends('room_ids.surface_disinsection')
    def _compute_surface_disinsection(self):
        surface_disinsection = 0.0
        for room in self.room_ids:
            surface_disinsection += room.surface_disinsection
        self.surface_disinsection = surface_disinsection

    @api.depends('room_ids.surface', 'surface_terraces', 'surface_cleaned_ext', 'surface_derating_ext')
    def _compute_all_surface(self):
        surface = {'office': 0.0, 'meeting': 0.0, 'lobby': 0.0, 'staircase': 0.0, 'kitchens': 0.0, 'sanitary': 0.0,
                   'laboratory': 0.0, 'it_endowments': 0.0, 'garage': 0.0, 'warehouse': 0.0, 'log_warehouse': 0.0,
                   'archive': 0.0, 'cloakroom': 0.0, 'premises': 0.0, 'access': 0.0, }

        for room in self.room_ids:
            surface[room.usage] += room.surface

        self.surface_office = surface['office']
        self.surface_meeting = surface['meeting']
        self.surface_lobby = surface['lobby']
        self.surface_staircase = surface['staircase']
        self.surface_kitchens = surface['kitchens']
        self.surface_sanitary = surface['sanitary']
        self.surface_laboratory = surface['laboratory']
        self.surface_it_endowments = surface['it_endowments']
        self.surface_garage = surface['garage']
        self.surface_warehouse = surface['warehouse']
        self.surface_log_warehouse = surface['log_warehouse']
        self.surface_archive = surface['archive']
        self.surface_cloakroom = surface['cloakroom']
        self.surface_premises = surface['premises']
        self.surface_access = surface['access']

        self.surface_common = surface['meeting'] + surface['lobby'] + surface['staircase'] + \
                              surface['kitchens'] + surface['sanitary'] + surface['access']

        self.surface_useful = surface['office'] + self.surface_common + surface['laboratory'] + \
                              surface['it_endowments'] + surface['garage'] + surface['warehouse'] + \
                              surface['log_warehouse'] + surface['archive'] + \
                              surface['cloakroom'] + surface['premises']

        self.surface_cleaned_adm = self.surface_common + surface['office']
        self.surface_cleaned_ind = surface['garage'] + surface['cloakroom'] + self.surface_terraces

        self.surface_cleaned_tot = self.surface_cleaned_adm + self.surface_cleaned_ind + self.surface_cleaned_ext

        self.surface_derating_int = self.surface_useful
        self.surface_derating = self.surface_derating_ext + self.surface_derating_int


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

class propertyBuildingTypes(models.Model):
    _name = 'property.building.type'
    _rec_name = 'nombre'

    codigo = fields.Char('Codigo Postal')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')
