from  odoo import fields,models,api

class SalesOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SalesOrder,self).action_confirm()
        for order in self:
            if order.partner_id:
                order.partner_id.last_contact_date = fields.Date.today()

        return res