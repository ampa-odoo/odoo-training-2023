from odoo import fields,models

class property(models.Model):
    _name = "real_estate.property"
    _description = "Property Model"

    name = fields.Char(string="Title",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    # expected_price = fields.Float('Expected Price', index=True,required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],default="north")
