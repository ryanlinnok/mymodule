# -*- coding: utf-8 -*-
{
    'name': "History Stock Report",
    'summary': """
        History Stock Report""",
    'description': """
        Fungsi dari modul untuk melihat history stock mulai dari saldo awal, masuk, keluar dan saldo akhir barang.
    """,
    'author': 'ryanlinnok',
    # 'images': ['static/description/images/main_screenshot.png'],
    'depends': ['base','purchase'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        'views/stock_view.xml',
        'wizard/wizard_history_stock_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 4,
    'currency': 'EUR',
}