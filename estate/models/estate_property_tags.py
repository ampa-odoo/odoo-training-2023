# -*- coding: utf-8 -*-

from odoo import fields, models


class estate_property_tags(models.Model):
    _name = "estate.property.tags"
    _description = "estate property tags model"

    name = fields.Char(string ="Name", required =True)
