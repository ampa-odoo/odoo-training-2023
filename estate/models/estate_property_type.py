# -*- coding: utf-8 -*-
from odoo import fields, models,api


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = "name"
    _sql_constraints = [
        ("unique_expected_price", "UNIQUE(name)", "Property Type must be unique"),
    ]

    name=fields.Char(string="Name",required=True)
    property_types_ids=fields.One2many('estate.property','property_type_id')
    sequence = fields.Integer(string="Sequence")
    offer_ids = fields.One2many('estate.property.offer','property_id',string="offer")
    offer_count = fields.Integer( string='Offers', compute='_compute_offer_count')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
           
    # Button
    def action_view_offer(self):
        if self.property_types_ids = 