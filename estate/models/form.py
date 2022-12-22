# -*- coding: utf-8 -*-


from odoo import models, fields
 
class realEstate(models.Model):
    _name = "real.state"
    _description = "This is the Database for the all clients and their requirements"

    name = fields.Char( "Name",required=True )
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date("Date Availability",default=lambda self: fields.Datetime.now())  
    expected_price = fields.Float( "Excepted Price")
    selling_price = fields.Float( "Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area",default="1")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden",default=1)
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        selection=[('small', 'Small'), ('big','Big')]
        )
