from odoo import fields,models

class CRMLead(models.Model):
    _inherit  = 'crm.lead'


    custom_activity_ids = fields.One2many('crm.activity','lead_id',string="Mahsus faoliyat")
