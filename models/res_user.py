from odoo import api, fields, models, tools, SUPERUSER_ID, _
from datetime import datetime

from odoo.odoo.exceptions import ValidationError


class beehivePartner(models.Model):
    _name = "property.property_admin"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto asociado")
    employee_id = fields.Many2one('hr.employee',
                                  string='Empleado relacionado', ondelete='restrict', auto_join=True,
                                  help='Employee-related data of the user')
    res_group_id = fields.Many2many('res.groups', 'rel_faculty_group', string="Assign Group", required=True)

    @api.model
    def create(self, vals):
        is_active = vals.get('is_active', False)
        if is_active:
            vals['is_active'] = True
        else:
            vals['is_active'] = True
        group_id = vals.get('res_group_id', False)
        login = vals.get('login', False)
        if login:
            vals['login'] = login.lower()
            vals['email'] = vals['login']
            user = self.env['res.users'].search([('login', '=', vals['login'])])
            if user:
                raise ValidationError('El usuario ya existe.')
            else:
                admin_group = self.env.ref('ofimatica_property.group_property_admin')
                # Create a custom user User
                self.env['res.users'].create({
                    'name': vals['name'],
                    'login': vals['login'],
                    'email': vals['email'],
                    'company_id': self.env.ref('base.main_company').id,
                    'groups_id':
                        admin_group,

                })
                # This code is to create an employee while creating an user.
                result = super(beehivePartner, self).create(vals)
                result['employee_id'] = self.env['hr.employee'].sudo().create({'name': result['name'],
                                                                               'user_id': result['id'],
                                                                               'address_home_id': result[
                                                                                   'partner_id'].id})
                partner = self.env['res.partner'].search([('id', '=', user.partner_id.id)])
                if partner:
                    partner.write({'email': vals['login']})


        return result


class beehiveOwner(models.Model):
    _name = "property.property_owner"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto Asociado")
    building_id = fields.Many2one('property.building', string="Inmueble asociado")

class beehiveLessee(models.Model):
    _name = "property.property_lessee"
    _inherit = "res.users"

    documento = fields.Char('No. Documento')
    land_id = fields.Many2one('property.land', string="Conjunto asociado")
    building_id = fields.Many2one('property.building', string='Inmueble asociado')
    patern_id = fields.Many2one('res.user', string="Propietario asociado")
    
#class updateResUsers(models.Model):
#    _inherit = "res.users"
#    land_id = fields.Many2one('property.land', string="Conjunto asociado")