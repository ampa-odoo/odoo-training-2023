# -*- coding: utf-8 -*-

from odoo import fields, models

class Real_estate(models.Model):
    _name="estate.property.model"
    _description="Real Estate Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='orientation',
    selection=[('North','A'),('East','B'),('West','C'),('South','D')])

