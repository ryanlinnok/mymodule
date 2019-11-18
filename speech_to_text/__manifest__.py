{
    'name': 'E-Notes',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Speech to Text',
    "description": """\

This module serves to facilitate inputting notes, E-Notes, which is a system that converts audiovisual speech into text

""",

    'author': 'ryanlinnok',
    'images': ['static/description/images/main_screenshot.png'],
    'depends': ['base'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        # 'security/ir.model.access.csv',
        'views/speech_to_text_view.xml',
        'views/speech_to_text_web.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 9,
    'currency': 'EUR',
}

