from odoo import fields,models






class CRMLead(models.Model):
    _inherit = 'crm.lead'

    inventory_warning = fields.Html(string="Ombor ogohlantirishi", readonly=True)

    def write(self,vals):
        res = super(CRMLead,self).write(vals)
        if 'stage_id' in vals:
            for lead in self:
                if lead.stage_id.is_won:
                    lead._check_inventory_availability()

        return res
    def _check_inventory_availability(self):
        for lead in self:
            orders = self.env['sale.order'].search([
                ('opportunity_id','=',lead.id)
            ])
            warnings = []
            for order in orders:
                for line in order.order_line:
                    product = line.product_id
                    if product.qty_available < line.product_uom_qty:
                        warnings.append(
                            "%s: kerak %s, omborda bor %s" % (
                            product.name,
                            line.product_uom_qty,
                            product.qty_available
                            )
                        )
            if warnings:
                massage = "⚠️ Omborda yetarli mahsulot yo'q:<br/>" + "<br/>".join(warnings)
                lead.inventory_warning = massage
                lead.message_post(body=massage)
            else:
                lead.inventory_warning = False



