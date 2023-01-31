{
    'name': "Real_estate",
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "Tejas Modi(temo)",
    'category': 'Real_estate/Brokerage',
    'description': "This is real estate module",
    'summary':'hello',
    'installable':'true',
    'application':'true',
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_menu.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/res_users_ad_views.xml',
        'reports/estate_property_templates.xml',
        'reports/property_res_user_templates.xml',
        'reports/estate_property_reports.xml',
    ],
     'demo':[
         'demo/estate_demo.xml',
         'demo/estate_propertytype_demo.xml',
         'demo/estate_propertytag_demo.xml',
     ]
}
