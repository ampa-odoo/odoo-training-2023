# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add
from odoo.exceptions import UserError

class estateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a regarding Real Estate"
    active = fields.Boolean(default=True)

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: add(fields.Datetime.now(), months=3), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(required=True, default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    state = fields.Selection(
        selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson_id = fields.Many2one('res.users', string="Sales Person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offer")

    total_area = fields.Integer(compute="_compute_total_area")
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    best_offer = fields.Float(compute="_compute_best_offer", default=0)
    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)

    def action_property_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Canceled Properties cannot be sold")
            record.state = 'sold'
        return True

    def action_property_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold Properties cannot be canceled")
            record.state = 'canceled'
        return True
