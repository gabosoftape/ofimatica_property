# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


from odoo import models, fields, api, _
from datetime import datetime


class PropertyProperty(models.AbstractModel):
    _name = 'property.property'
    _description = "Property"
    _inherit = 'mail.thread'


    def _default_company(self):
        return self.env['res.company']._company_default_get(self._name)

    name = fields.Char(string="Nombre")
    foto = fields.Binary()
    street = fields.Char(string="Direccion", required=True)
    street2 = fields.Char()
    zip = fields.Char(string="Codigo Postal", change_default=True)
    city = fields.Char(string="Ciudad", required=True)
    state_id = fields.Many2one("res.country.state", string='Estado', ondelete='restrict',required=True)
    country_id = fields.Many2one('res.country', string='País', ondelete='restrict')
    company_id = fields.Many2one('res.company', 'Compañia', index=True, default=_default_company)
    active = fields.Boolean(default=True)
    nit = fields.Char(string="NIT")
    asset_number = fields.Char(string="NIIF", index=True)



    class_number = fields.Char(string="Class")
    class_code = fields.Char(string="Codigo de clasificacion")
    cost_center_id = fields.Many2one('property.cost.center',string='Centro de costos')
    order_number = fields.Char(string='Numero de orden')


    acquisition_mode_id = fields.Many2one('property.acquisition', string="Modo de adquisision")
    date_acquisition = fields.Date(string="Fecha de adquisicion")
    doc_acquisition = fields.Char(string="Documento de adquisicion")

    surface = fields.Float(string="Area")

    note = fields.Text()

    doc_count = fields.Integer(string="Numero de documentos", compute='_get_attached_docs')


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




    @api.model
    def default_get(self, fields):
        defaults = super(PropertyProperty, self).default_get(fields)

        defaults['country_id'] = self.env.user.company_id.partner_id.country_id.id
        return defaults

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}
