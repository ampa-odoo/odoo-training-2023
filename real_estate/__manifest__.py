# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'mobe',
    'category' :'Marketing',
    'data' : [
         'security/ir.model.access.csv',
         'views/estate_property_menus.xml',
         'views/estate_property_views.xml',
         'views/property_type_views.xml',
         'views/property_tags_views.xml',
         'views/property_offer_views.xml',
         

    ],
    'demo' : [
        'demo/estate_properties_demo.xml',
        'demo/estate_property_type_demo.xml',
        'demo/estate_property_tag_demo.xml',

    ],
    'application' : True,
    'installable' :True,
    'auto_install' : False,
}