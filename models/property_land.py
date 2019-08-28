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

    location_type = fields.Selection([('CR', 'Conjunto Residencial'), ('E', 'Edificio')], default='CR')

    tarla = fields.Char('Telefono')  # required=True)
    parcela = fields.Char(string="Foto")
    sector = fields.Char(string="Sector catastral")
    bloc_fizic = fields.Char(string="Cedula catastral")

    carte = fields.Char(string="Carte funciară")
    utr = fields.Char(string="UTR")
    categ_id = fields.Many2one('property.land.categ', string="Categoría")
    cod = fields.Char()


class tipoDePropiedad(models.Model):
    _name = 'property.land.type'

    codigo = fields.Char('Referencia', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion')


