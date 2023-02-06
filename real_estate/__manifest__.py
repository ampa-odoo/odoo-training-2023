{
    'name': 'Real Estate',
    'application':True,
    'version': '1.0',
    'depends': ['base'],
    'author': 'PRPA',
    'category': 'Category',
    'summary': 'Real Estate Module Training',
    'license': 'LGPL-3',
    'installable': True,
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ] 
}