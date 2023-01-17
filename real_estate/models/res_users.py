# -*- coding: utf-8 -*-

from odoo import fields, models

class inheriteduser(models.Model):
    _inherit = "res.users"


    property_ids = fields.One2many("estate.property","salesman_id",string="Properties", domain=[("state", "in", ["new", "offer_received"])])