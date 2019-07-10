from odoo import api, fields, models, _
import time
from datetime import date, datetime, timedelta
from odoo.exceptions import except_orm, Warning, RedirectWarning

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    @api.multi
    def button_confirm(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            order._add_supplier_to_product()

            result = {}
            for rec in self.order_line:
                inventory_line_ids = self.env['stock.inventory.line'].search([('product_id','=',rec.product_id.id),
                                                                          ('inventory_id.state','=','confirm'),
                                                                         ])

                if inventory_line_ids:
                    for inventory in inventory_line_ids :
                        result = {
                                'inventory_id': inventory.inventory_id.id,
                                'purchase_id' : self.id,
                                'type_id' : 'purchase',
                        }
                    inventory_storage_ids = self.env['inventory.storage'].create(result)
                    self.write({'state': 'purchase', 'date_approve': fields.Date.context_today(self)})
                    return inventory_storage_ids

                else:
                    # Deal with double validation process
                    if order.company_id.po_double_validation == 'one_step'\
                            or (order.company_id.po_double_validation == 'two_step'\
                                and order.amount_total < self.env.user.company_id.currency_id.compute(order.company_id.po_double_validation_amount, order.currency_id))\
                            or order.user_has_groups('purchase.group_purchase_manager'):
                        order.button_approve()
                    else:
                        order.write({'state': 'to approve'})
        return True