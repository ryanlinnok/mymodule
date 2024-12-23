{
    'name': 'Stock History',
    'version': '1.0',
    'category': 'Stock',
    'summary': 'Stock History',
    "description": """\

Modul ini berfungsi untuk memudahkan dalam melihat riwayat stock

""",

    'author': 'ryanlinnok',
    'depends': ['stock'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        # 'security/ir.model.access.csv',
        "views/stock_view.xml",
        "views/wizard_history_stock_view.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 4,
    'currency': 'EUR',
}