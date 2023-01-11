from odoo import api,fields,models
from dateutil.relativedelta import relativedelta
from datetime import date

class Estate_property_offer(models.Model):
    _name= "estate.property.offer"
    _description= "Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(string="Status", selection=[('accepted','Accepted'),('refused','Refused')],default=" ",copy=False)
    partner_id= fields.Many2one("res.partner",required=True)
    property_id= fields.Many2one("estate.property.model",required=True)
    validity = fields.Integer(default="7")
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")


    @api.depends('validity','create_date')
    def _compute_deadline(self):

        for record in self:
            # print("-----------------", record.create_date)
            if record.create_date == True:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = date.today() + relativedelta(days=record.validity)


    def _inverse_deadline(self):
        
        for record in self:  
            record.validity=abs(record.create_date.date() - record.date_deadline).days
            
            # record.validity = (record.date_deadline - record.create_date.date()).days
        

    def action_accept(self):

        for record in self:

            record.property_id.offer_ids.status='refused'
            record.status='accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            # copied it from dhrp
            # record.status='accepted'
            # # print(record.status)
            # record.property_id.buyer_id=record.partner_id
            # record.property_id.selling_price=record.price

        # for record in self:
        #     print(record.status)
        
        
        

    # def action_accept(self):

    #     for record in self:
    #         print(record)
        # for record in self:
        #     record.status='accepted'

        # for record.status in self:
        #     if record.status != 'accepted':
        #        record.status = 'refused'

    
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)',
         'The offer Price Should Be Positive'),
     
    ]
    
    def action_refuse(self):

        # for record in self:
        #     record.status='refused'
        self.status = 'refused'
