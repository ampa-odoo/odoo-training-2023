# -*- coding: utf-8 -*-
{
    'name': ' Real estate',
    'category': 'sales',
    'summary': ' For buying and selling proerties.',
    'description': ' This is a  real estate Module',
    'author': 'Karnav',
    'depends': [],
    'sequence': 1,
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/estate_menu.xml',
    ],
    'demo':[
        'demo/estate_property_demo.xml',
    ],
    'depends' : ['mail'],
}
