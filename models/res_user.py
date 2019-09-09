from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')

class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')