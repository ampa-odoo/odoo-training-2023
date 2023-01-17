# -*- coding: utf-8 -*-

from odoo import fields, models

class inheritedModel(models.Model):
    _name = "res.users"
    # _inherit = 'res.users'

    # property_ids = fields.One2many("estate.property", "salesperson_id", string = "Properties")
    demo=fields.Char()

class inheritedModel1(models.Model):
    _name = "inherited.model1"

    demo1 = fields.Char()

class inheritedModel2(models.Model):
    _name = "inherited.model2"
    
    _inherits={'res.users': 'demo_id',
                'inherited.model1': 'demo1_id'}

    name = fields.Char()

    demo_id = fields.Many2one("res.users")
    demo1_id = fields.Many2one("inherited.model1")
