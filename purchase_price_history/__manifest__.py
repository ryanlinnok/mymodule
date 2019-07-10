{
    'name': 'Purchase Price History',
    'version': '1.0',
    'category': 'Purchase',
    'summary': 'Purchase Price History',
    "description": """\

Modul ini berfungsi untuk memudahkan dalam melihat riwayat harga pembelian

""",

    'author': 'ryanlinnok',
    'images': ['static/description/images/main_screenshot.png'],
    'depends': ['base','purchase'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        # 'security/ir.model.access.csv',
        "views/product_product_view.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 19,
    'currency': 'EUR',
}