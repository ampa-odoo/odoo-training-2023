{
    'name':'Real Estate',
    'version':'0.1',
    'depends':['base'],
    'author':'Harsh Modi (hamo)',
    'category':'Sales',
    'data':[
        'security/ir.model.access.csv',
        'views/real_estate_property_views.xml',
        'views/real_estate_property_offer_views.xml',
        'views/real_estate_property_type_views.xml',
        'views/real_estate_property_tags_views.xml',
        'views/real_estate_menus.xml'
    ],
    'demo':['data/real_estate_property_demo.xml',],
    'summary':'A real estate module',
   'installable':'true',
   'application':'true',
}