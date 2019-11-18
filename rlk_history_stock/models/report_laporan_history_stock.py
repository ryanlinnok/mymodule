from odoo import models, fields, api
from odoo.exceptions import except_orm, Warning, RedirectWarning
from datetime import date, datetime, timedelta


class report_laporan_history_stock(models.AbstractModel):

    _name = 'report.rlk_history_stock.report_laporan_history_stock'
    _template = 'rlk_history_stock.report_laporan_history_stock'

    @api.multi
    def _get_history_stock_line(self, data):
        domain = []

        date_start_convert = ''
        date_stop_convert = ''

        if data['date_start'] and data['date_stop'] and data['product_id'] and data['lokasi_id']:
            date_start_convert = datetime.strptime(data['date_start'] + " 00:00:00", '%Y-%m-%d %H:%M:%S')
            date_stop_convert = datetime.strptime(data['date_stop'] + " 23:59:59", '%Y-%m-%d %H:%M:%S')
            date_start_convert = date_start_convert.strftime("%Y-%m-%d %H:%M:%S")
            date_stop_convert = date_stop_convert.strftime("%Y-%m-%d %H:%M:%S")
            domain = [
                ('date','>=',date_start_convert),
                ('date','<=',date_stop_convert),
                ('location_id','=', data['lokasi_id']),
                ('product_id','=',data['product_id']),
                ]

            
        stock_ids = self.env['stock.history'].search(domain, order='date asc')    
        value = []
        result = {}

        price_unit = 0
        jumlah_keluar = 0

        for stock in stock_ids:
            price_unit = stock.product_id.hpp

            if stock.quantity < 0:
                jumlah_keluar = 0 - stock.quantity
                    
                result = {
                        'tanggal_update': stock.date,
                        'stock_move': '[' + stock.move_id.location_id.name + ']' + ' ke ' + '[' + stock.move_id.location_dest_id.name + ']',
                        'no_transaksi' : stock.move_id.picking_id.partner_id.name,
                        'jumlah_masuk'    : 0,
                        'jumlah_keluar'   : jumlah_keluar,
                        'saldo_awal' : stock.saldo_awal,
                        'saldo_akhir' : stock.saldo_awal - jumlah_keluar,
                        'hpp' : '{:0,.2f}'.format(price_unit),
                        'keterangan' : stock.move_id.picking_id.name,
                        'petugas' : stock.move_id.create_uid.name,
                }
            if stock.quantity > 0:
                    
                result = {
                        'tanggal_update': stock.date,
                        'stock_move': '[' + stock.move_id.location_id.name + ']' + ' ke ' + '[' + stock.move_id.location_dest_id.name + ']',
                        'no_transaksi' : stock.move_id.picking_id.partner_id.name,
                        'jumlah_masuk'    : stock.quantity,
                        'jumlah_keluar'   : 0,
                        'saldo_awal' : stock.saldo_awal,
                        'saldo_akhir' : stock.saldo_awal + stock.quantity,
                        'hpp' : '{:0,.2f}'.format(price_unit),
                        'keterangan' : stock.move_id.picking_id.name,
                        'petugas' : stock.move_id.create_uid.name,
                }

            value.append(result)

        return value


    @api.multi
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        docargs = {
            'data': data['form'],
            'get_history_stock_line': self._get_history_stock_line,
            'doc_ids': self.ids,
            'doc_model': model,
            'docs': docs
        }

        return report_obj.render(self._template, docargs)


