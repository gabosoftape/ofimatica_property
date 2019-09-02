from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime
from odoo.modules import get_module_resource

class Partner(models.Model):
    _inherit = "res.users"

    tipo = fields.Selection(selection=[('administrador_super','SA'),
                                           ('administrador','Administrador'),('propietario','Propietario'),('arrendatario','Arrendatario')])
    documento = fields.Char('No. Documento')