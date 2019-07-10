from odoo import api, fields, models, _
import time
from datetime import date, datetime, timedelta
from odoo.exceptions import except_orm, Warning, RedirectWarning


class ProductProduct(models.Model):
    _inherit = 'product.template'

    history_price_ids = fields.One2many('product.history.price', 'product_id', 'Product History Price')

class ProductHistoryPrice(models.Model):
    _name = "product.history.price"

    product_id = fields.Many2one('product.product','Product') 
    price = fields.Float('Price')
    date = fields.Datetime('Date')