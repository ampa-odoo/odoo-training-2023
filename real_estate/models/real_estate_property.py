# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta

from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This model will store the price related to estate"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Address of the building")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(copy=False, default=fields.datetime.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = "Type",
        selection = [("north", "North"), ("south", "South"), ("west", "West"), ("east", "East")]
    )
    active = fields.Boolean(default=True, string="Active")
    state = fields.Selection([("new","New"),("recieved","Offer Recieved"),("accepted","Accepted"),("sold","Sold"),("cancel","Canceled")], string="Status", copy=False, default="new")
    property_type_id = fields.Many2one("estate.property.type")
    buyer_id = fields.Many2one("res.partner", copy=False)
    seller_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", 'property_id')



