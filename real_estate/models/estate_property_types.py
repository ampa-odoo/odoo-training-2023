from odoo import fields,models

class Property_type(models.Model):
    _name = "estate.property.type"
    _description = "Estate property types"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_type_name','unique(name)','Type name must be unique'),
    ]
    