from odoo import api, fields, models, _
import time
from datetime import date, datetime, timedelta
from odoo.exceptions import except_orm, Warning, RedirectWarning

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.multi
    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))
        self._action_confirm()
        if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
            self.action_done()
        return True


    @api.multi
    def action_confirm_new(self):
        res = super(SaleOrder, self).action_unlock()
        for order in self.order_line:
            inventory_line_ids = self.env['stock.inventory.line'].search([('product_id','=',order.product_id.id),
                                                                          ('inventory_id.state','=','confirm'),
                                                                         ])

            if inventory_line_ids:
                for inventory in inventory_line_ids :
                    result = {
                            'inventory_id': inventory.inventory_id.id,
                            'sale_id' : self.id,
                            'type_id' : 'sale',
                    }
                inventory_storage_ids = self.env['inventory.storage'].create(result)
                if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
                    self.action_done()
                return res

            else:
                self.action_confirm()