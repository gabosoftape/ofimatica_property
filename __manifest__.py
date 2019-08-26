# -*- coding: utf-8 -*-
# ©  2018-2019 gabosoft
#              gabriel pabon <gabosoft.ape(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Property Management",
    'version': '12.0.1.0.0',
    "author": "Ofimatica Soluciones, Gabriel Pabon",
    "website": "https://www.ofimaticasoluciones.com",

    "category": "Property",
    "depends": [
        'mail',
    ],
    "license": "LGPL-3",
    "data": [
        'views/property_menu_view.xml',
        'views/property_config_view.xml',
        'views/property_land_view.xml',
        'views/property_building_view.xml',
        'views/property_room_view.xml',
        'data/data.xml',
        'data/res.country.state.csv',
        'security/ir.model.access.csv'

    ],
    'application': True,
    "images": ['images/main_screenshot.png'],
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
