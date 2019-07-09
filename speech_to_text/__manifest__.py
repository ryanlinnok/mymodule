{
    'name': 'E Notula',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Speech to Text',
    'description':"""Modul ini berfungsi untuk memudahkan dalam penginputan notulen, E Notula yaitu suatu sistem yang mengubah ucapan audiovisual menjadi text""",
    'author': 'ryanlinnok',
    'depends': ['base'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        # 'security/ir.model.access.csv',
        'views/speech_to_text_view.xml',
        # 'views/dashboard_iframe_view.xml',
        'views/speech_to_text_web.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'price': 99,
    'currency': 'EUR',
}

