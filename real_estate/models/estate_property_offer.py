# -*- coding:utf:8 -*-

from odoo import models, fields, api
from odoo.tools.date_utils import add


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Offer module"

    price = fields.Float("Price")
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    validity = fields.Integer()
    date_deadline = fields.Date(
        "Date Deadline", compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    create_date = fields.Date(default=fields.Datetime.now(), readonly=True)

    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = add(record.create_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date).days
