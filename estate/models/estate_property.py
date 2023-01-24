# -*- coding: utf-8 -*-
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta



class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=fields.Date.today()+relativedelta(months=3), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancel', 'Canceled'), ], string='State',tracking=True,default='new', copy=False)
    property_type_id = fields.Many2one("estate.property.type",string="Property Type")
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user) 
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many("estate.property.tag","property_tag_rel","property_id","tag_id", string="Property tag")
    offer_ids = fields.One2many('estate.property.offer','property_id',string="offer")
    # computed fields
    total_area = fields.Integer(string="Total Area (sqm)",compute = "_compute_total_area")
    best_price = fields.Float(string="Best offer",compute="_compute_best_price")
    garden_area = fields.Integer(string="Garden Area (sqm)",compute='_compute_garden_area',store=True,readonly=False)
    garden_orientation = fields.Selection(
        [('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')],compute='_compute_garden_orientation',readonly=False)

    # Compute Method
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price"),default=0)
    @api.depends("garden")
    def _compute_garden_area(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
            else:
                record.garden_area = 0
    @api.depends("garden")
    def _compute_garden_orientation(self):
        for record in self:
            if record.garden:
                record.garden_orientation = 'north'
            else:
                record.garden_orientation = ''
    # BUTTONS
    # def action_sold(self):
    #     if self.state != 'cancel':
    #     # for record in self:
    #     #     record.state = "sold"
    #     #     else
    #     # return True
    # def action_cancel(self):
    #     for record in self:
    #         record.state = "cancel"
    #     return True
