from odoo import api, fields, models, _
import time
from datetime import date, datetime, timedelta
from odoo.exceptions import except_orm, Warning, RedirectWarning

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_approve(self, force=False):
        self.write({'state': 'purchase', 'date_approve': fields.Date.context_today(self)})
        self._create_picking()
        self.filtered(
            lambda p: p.company_id.po_lock == 'lock').write({'state': 'done'})

        for rec in self.order_line:
            product_id = self.env['product.product'].search([('id','=',rec.product_id.id)],limit=1)
            if product_id:
                price_ids = self.env['product.history.price'].sudo().create({
                    'product_id' : rec.product_id.id,
                    'date' : datetime.now(),
                    'price' : rec.price_unit,
                })

        return {}