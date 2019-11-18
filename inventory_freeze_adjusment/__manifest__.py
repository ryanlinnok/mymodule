{
    'name': 'Inventory Freeze Adjusment',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Inventory Freeze Adjusment',
    "description": """\

Modul ini berfungsi untuk memudahkan Stock Opname, Aktifitas Sales dan Purchase tetap berjalan.

""",

    'author': 'ryanlinnok',
    'images': ['static/description/images/main_screenshot.png'],
    'depends': ['base','purchase','sale_management'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        # 'security/ir.model.access.csv',
        "views/inventory_storage_view.xml",
        "views/sale_view.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 9,
    'currency': 'EUR',
}