from odoo import models, fields,api



class CrmActivity(models.Model):
    _name = 'crm.activity'
    _description = "CRM Activity"

    partner_id = fields.Many2one('res.partner',string="Contact",compute='_compute_partner_id',store=True,readonly=False)
    user_id = fields.Many2one('res.users',string="User")
    activity_type = fields.Selection([("call","Qo'ng'iroq"),("meeting","Uchrashuv"),("email","email")],string="Selection")
    date_time = fields.Datetime(string="Date Time")
    text = fields.Text(string='Description')
    lead_id = fields.Many2one('crm.lead',string='Opportunity')

    @api.depends('lead_id','lead_id.partner_id')
    def _compute_partner_id(self):
        for activity in self:
            if activity.lead_id and activity.lead_id.partner_id:
                activity.partner_id = activity.lead_id.partner_id