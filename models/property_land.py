# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import models, fields, api
from datetime import datetime


class beehiveCompanies(models.Model):
    _name = 'property.company'
    _inherit = 'res.company'

    location_type = fields.Many2one('property.land.type', string="Tipo de Copropiedad")
    tarla = fields.Char('Telefono')  # required=True)
    sector = fields.Char(string="Sector catastral")
    bloc_fizic = fields.Char(string="Cedula catastral")
    name = fields.Char(string="Nombre de Cliente")
    empresa_admin_doc_type = fields.Selection([('nit','Empresa Administradora'),('cc','Persona Natural')], string="Tipo de Administracion")
# aqui van los atributos de la primera entrega.
    empresa_admin = fields.Char('Nombre de Empresa Administradora')
    empresa_admin_nit = fields.Char('Nit')
    representante_legal = fields.Char(string="Representante legal")
    administrador_delegado = fields.Many2one('property.property_admin',string="Administrador Delegado")
    area_total = fields.Float(string="Area Total")
    area_comun = fields.Float(string="Area Comun" )
    localidad = fields.Many2one('property.localidad',string="Localidad")
    active = fields.Boolean(default=True)
    nit = fields.Char(string="NIT")
    doc_count = fields.Integer(string="Numero de documentos", compute='_get_attached_docs')
    foto = fields.Binary(required=True)
    note = fields.Text()

    @api.multi
    def _get_attached_docs(self):
        for record in self:
            domain = [('res_model', '=', self._name), ('res_id', '=', record.id)]
            record.doc_count = self.env['ir.attachment'].search_count(domain)

    @api.multi
    def attachment_tree_view(self):
        domain = [('res_model', '=', self._name), ('res_id', 'in', self.ids)]
        return {
            'name': 'Documentos',
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }

class tipoDePropiedad(models.Model):
    _name = 'property.land.type'
    _rec_name = 'nombre'

    codigo = fields.Char('ID', required=True)
    nombre = fields.Char('Tipo de Copropiedad', required=True)
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


