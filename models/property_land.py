# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import models, fields, api
from datetime import datetime


class PropertyLand(models.Model):
    _name = 'property.land'
    _description = "Clientes"
    _inherit = 'property.property'

    location_type = fields.Many2one('property.land.type', string="Tipo de inmueble")
    tarla = fields.Char('Telefono')  # required=True)
    sector = fields.Char(string="Sector catastral")
    bloc_fizic = fields.Char(string="Cedula catastral")
    name = fields.Char(string="Nombre de Cliente")

    carte = fields.Char(string="Carte funciară")
    utr = fields.Char(string="UTR")
    cod = fields.Char()
    empresa_admin_doc_type = fields.Selection([('nit','Empresa Administradora'),('cc','Persona Natural')], string="Tipo de Administracion")
# aqui van los atributos de la primera entrega.
    empresa_admin = fields.Char('Nombre de Empresa Administradora')
    empresa_admin_nit = fields.Char('Nit')
    representante_legal = fields.Many2one('res.users',string="Representante legal")
    administrador_delegado = fields.Many2one('res.users',string="Administrador Delegado")
    area_total = fields.Float(string="Area Total")
    area_comun = fields.Float(string="Area Comun" )
    localidad = fields.Many2one('property.localidad',string="Localidad")

class tipoDePropiedad(models.Model):
    _name = 'property.land.type'
    _rec_name = 'nombre'

    codigo = fields.Char('Referencia', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion')

class localidadbehive(models.Model):
    _name = 'property.localidad'
    _rec_name = 'nombre'
    codigo = fields.Char('Codigo Postal')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')


class propertyBuildingTypes(models.Model):
    _name = 'building.type'
    _rec_name = 'nombre'
    codigo = fields.Char('Codigo')
    nombre = fields.Char('Nombre')
    descripcion = fields.Char('Descripcion')
