from odoo import api, fields, models, _
import time
from datetime import date, datetime, timedelta
from odoo.exceptions import except_orm, Warning, RedirectWarning

class InventoryStorage(models.Model):
    _name = "inventory.storage"
    _rec_name = "inventory_id"
            
    purchase_id = fields.Many2one('purchase.order', 'Purchase Order Ref#') 
    sale_id = fields.Many2one('sale.order', 'Sale Order Ref#') 
    type_id = fields.Selection([('sale','Sale'),('purchase','Purchase'),('internal_use','Internal Use')], 'Type') 
    inventory_id = fields.Many2one('stock.inventory', 'Inventory Adjustments')


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    def action_done(self):
        inventory_storage_po_ids = self.env['inventory.storage'].search([('inventory_id','=',self.id),('type_id','=','purchase')])
        if inventory_storage_po_ids:
            for storage in inventory_storage_po_ids:
                storage.purchase_id._create_picking()

        inventory_storage_sale_ids = self.env['inventory.storage'].search([('inventory_id','=',self.id),('type_id','=','sale')])
        if inventory_storage_sale_ids:
            for storage in inventory_storage_sale_ids:
                storage.sale_id.action_confirm()

        negative = next((line for line in self.mapped('line_ids') if line.product_qty < 0 and line.product_qty != line.theoretical_qty), False)
        if negative:
            raise UserError(_('You cannot set a negative product quantity in an inventory line:\n\t%s - qty: %s') % (negative.product_id.name, negative.product_qty))
        self.action_check()
        self.write({'state': 'done'})
        self.post_inventory()
        return True