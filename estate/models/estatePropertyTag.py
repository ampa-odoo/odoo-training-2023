# -- coding: utf-8 --

from odoo import fields,models


class estateProperty(models.Model):
    _name = "estate.property.tags"
    _description="property type model"

    name=fields.Char(string="Property type",required=True)