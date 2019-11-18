from datetime import datetime
from odoo import models, fields, api


class laporan_history_stock_wizard(models.TransientModel):
    _name = "laporan.history.stock.wizard"
    _description = "Laporan History Stock"

    date_start = fields.Date('Start Date', required=True)
    date_stop  = fields.Date('End Date', required=True)
    company_id = fields.Many2one('res.company', string='Organisasi', default=lambda self:self.env.user.company_id.id)
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    gudang_id = fields.Many2one(comodel_name='stock.warehouse', string='Gudang')
    location_id = fields.Many2one(comodel_name='stock.location', string='Lokasi')

    @api.onchange('company_id')
    def _get_gudang(self):
        stock_warehouse = self.env['stock.warehouse'].search([('company_id','=',self.company_id.id)])
        for rec in stock_warehouse:
            self.gudang_id = rec.id

    @api.multi
    def generate_report(self):
        tgl = datetime.now().day
        convert_date_month = datetime.now().month
        year = datetime.now().year

        month = ''
        date_print = ''

        if convert_date_month == 01:
            month = 'Januari'
        if convert_date_month == 02:
            month = 'Februari'
        if convert_date_month == 03:
            month = 'Maret'
        if convert_date_month == int('04'):
            month = 'April'
        if convert_date_month == 05:
            month = 'Mei'
        if convert_date_month == 06:
            month = 'Juni'
        if convert_date_month == 07:
            month = 'Juli'
        if convert_date_month == int('08'):
            month = 'Agustus'
        if convert_date_month == int('09'):
            month = 'September'
        if convert_date_month == 10:
            month = 'Oktober'
        if convert_date_month == 11:
            month = 'November'
        if convert_date_month == 12:
            month = 'Desember'

        date_print = str(tgl) + ' ' + month + ' ' + str(year)

        lokasi_name = 'Lokasi belum diisi'
        if self.location_id:
            lokasi_name = self.location_id.name

        report_obj = self.env['report']
        template = 'rlk_history_stock.report_laporan_history_stock'
        report = report_obj._get_report_from_name(template)
        domain = {
            'date_start': self.date_start,
            'date_stop': self.date_stop,
            'company_id': self.company_id.id,
            'company_name': self.company_id.name,
            'company_address': self.company_id.street,
            'company_phone': self.company_id.phone,
            'tanggal_print': date_print,
            'gudang_id': self.gudang_id.id,
            'gudang_name': self.gudang_id.name,
            'lokasi_id': self.location_id.id or False,
            'lokasi_name': lokasi_name,
            'product_id': self.product_id.id,
            'product_name': self.product_id.name,
            'uom_po_id': self.product_id.uom_po_id.id,
            'uom_po_name': self.product_id.uom_po_id.name,
        }
        values = {
            'ids' : self.ids,
            'model' : report.model,
            'form': domain
        }
        return report_obj.get_action(self, template, data=values)
 
