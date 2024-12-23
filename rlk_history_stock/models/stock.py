# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
import calendar
import warnings
import time
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.exceptions import except_orm, Warning, UserError, RedirectWarning


class StockHistory(models.Model):
    _inherit = 'stock.history'

    saldo_awal = fields.Float('Saldo Awal', compute='_get_saldo_awal')

    @api.one
    def _get_saldo_awal(self):
        current_sequence = 0
        for rec in self:
            if rec.date:

                self._cr.execute('SELECT q.qty as qty FROM stock_quant q WHERE location_id = %s AND product_id = %s', (rec.location_id.id, rec.product_id.id))
                onhand_ids = self.env.cr.dictfetchall()

                self._cr.execute('SELECT qh.quantity as quantity FROM stock_history qh WHERE location_id = %s AND product_id = %s', (rec.location_id.id, rec.product_id.id))
                qty_history_ids = self.env.cr.dictfetchall()

                qty_onhand_location = sum(q.get('qty') for q in onhand_ids)
                qty_history_location = sum(q.get('quantity') for q in qty_history_ids)
                saldo_awal = qty_onhand_location - qty_history_location

                self._cr.execute('SELECT history.quantity as quantity, history.id as history_id FROM stock_history history WHERE location_id = %s AND product_id = %s AND date < %s', (rec.location_id.id, rec.product_id.id, rec.date))
                history_ids = self.env.cr.dictfetchall()
                index = 0
                for d in history_ids:
                    index += 1
                    if d.get('history_id') == rec.id:
                        current_sequence = index
                        saldo_awal += d.get('quantity')
                    else:
                        saldo_awal += d.get('quantity')

            else:
                current_sequence = 0

            rec.saldo_awal = saldo_awal