# -*- coding: utf-8 -*-

{
    'name': "Real Estate",
    'version': '1.0',
    'author': "yava",
    'description': "You can easily apply your core project modual with odoo's Real Estate ",
    'data': [
        'security/ir.model.access.csv',
        'data/estate_menus.xml',
        'views/estate_property_views.xml',
    ],
    'demo' :[

        'demo/estate_property_demo_data.xml'
        
    ],
    'application': True,
    'installable': True,
    'license' : "LGPL-3",
    'website': 'https://www.odoo.com',


}