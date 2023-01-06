from odoo import models,fields
from datetime import date
from dateutil.relativedelta import relativedelta

class Estate(models.Model):
    _name="real.estate.properties"
    _description="Property Model"

    name=fields.Char(string="Title",required=True)
    description=fields.Text('Description')
    postcode=fields.Char('Postcode')
    date_availability=fields.Date('Date Availabilty',copy=False,default=date.today()+relativedelta(months=3))
    expected_price=fields.Float('Expected Price',required=True)
    selling_price=fields.Float('Selling Price',required=True,copy=False)
    bedrooms=fields.Integer('Bedrooms',default=2)
    living_area=fields.Integer('Living Area')
    facades=fields.Integer('Facades')
    garage=fields.Boolean('Garage')
    garden=fields.Boolean('Garden')
    type_id=fields.Many2one('real.estate.property.type',string="Property type")
    garden_orientation=fields.Selection(selection=[('north','North'), ('south','South'), ('east','East'),('west','West')],default='north')
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[('new','New'),('offer recevied','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],default='new' ,copy=False)