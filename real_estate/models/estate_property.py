# -*- coding: utf-8 -*-
from odoo import models,fields

from dateutil.relativedelta import relativedelta

class estate_property(models.Model):
    _name = 'estate.property'
    _description = "Real Estate Module"

    property_type_id = fields.Many2one('estate.property.type',string='property type')

    name = fields.Char('Property Name',required=True)
    description = fields.Char('Description')
    postcode = fields.Char('PostCode')
    date_availability = fields.Date('Date',copy=False)
    #from dateutil.relativedelta(months=3)
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',readonly=True,copy=False)
    bedrooms = fields.Integer('Bedrooms',default='2')
    living_area = fields.Integer('living area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage',default=True)
    garden = fields.Boolean('Garden',default=True)
    garden_area = fields.Integer('Garden_area')
    garden_orientation = fields.Selection(
            string='Garden_orientation',default="North",
            selection=[('North','North'),('South','South'),('East','East'),('West','West')],
            help="This type is saparate north ,south,east and wast")
    active = fields.Boolean('Active',default=True)

    status = fields.Selection(
            string='Status',copy=False,default='New',
            selection=[('New','New'),('offer received','offer received'),('offer Accepted','offer Accepted'),('offer cancelled','offer cancelled'),('Sold','Sold')])
    #,default=lambda self: fields.Datetime.now()