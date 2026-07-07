from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    last_contact_date = fields.Date(string="Last contact date")
    total_due_amount = fields.Monetary(string='Total due amount', compute='_compute_total_due_amount', store=True,currency_field="currency_id")
    unpaid_invoice_count  = fields.Integer(string='Invoice count',compute='_compute_invoice_count',store=True)
    crm_activity_ids = fields.One2many('crm.activity','partner_id',string='activities')


    @api.depends('invoice_ids.amount_residual', 'invoice_ids.state', 'invoice_ids.payment_state')
    def _compute_total_due_amount(self):
        for partner in self:
            invoices = partner._get_unpaid_invoices()
            partner.total_due_amount = sum(invoices.mapped('amount_residual'))


    @api.depends('invoice_ids.amount_residual','invoice_ids.state','invoice_ids.payment_state')
    def _compute_invoice_count(self):
        for partner in self:
            invoice = partner._get_unpaid_invoices()
            partner.unpaid_invoice_count = len(invoice)

    def _get_unpaid_invoices(self):
        return self.invoice_ids.filtered(
            lambda inv: inv.move_type == "out_invoice"
                        and inv.state == 'posted'
                        and inv.payment_state != 'paid'
        )

    @api.constrains('last_contact_date')
    def _check_last_contact_date(self):
        for partner in self:
            if partner.last_contact_date  and partner.last_contact_date > fields.Date.today():
               raise ValidationError("Siz Kelajak Sanasini kiritdingiz")