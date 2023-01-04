# -*- coding: utf-8 -*-

from odoo import models,_,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.tools.date_utils import add
from odoo.exceptions import ValidationError

class estatepropertyoffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers Model"

    price = fields.Float(string="Property Price:")
    status = fields.Selection(selection=[('accepted','Accepted'),('refuse','Refused')])
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Property",required=True)
    validity = fields.Integer(string="Validity in Months",default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date",inverse="_inverse_deadline_date")
    create_date=fields.Date(default=lambda self:fields.Datetime.today())

    _sql_constraints=[
        ('check_Offer_price','CHECK(price >= 0)','Offer Price cannot be negative')
    ]

    @api.depends('validity','date_deadline')
    def _compute_deadline_date(self):
        for record in self:
            record.date_deadline= add(fields.Datetime.today(),days=record.validity)

    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
    
    @api.depends('status')
    def action_accept(self):
        for rec in self.search([('status','=','accepted')]):
            raise ValidationError(_("cannot accept more than one offer"))
        self.status='accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyers_id = self.partner_id

    def action_refuse(self):
        for record in self:
            if record.status == 'accepted':
                record.status = 'refuse'
