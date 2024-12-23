# -*- coding: utf-8 -*-
{
    'name': "X2ManyList",
    'summary': """
        Remove Add an Item Button & Trash Icon in x2Many Fields or Hide Add an Item Button & Trash Icon in x2Many Fields""",
    'description': """
        This module is designed to remove or hide the "Add an Item" button and trash icon in x2Many fields when the status is not in draft. However, other columns can still be edited.
    """,
    'author': 'ryanlinnok',
    'depends': ['web'],
    'website': 'https://ryanlinnok.github.io',
    'data': [
        'static/src/xml/backend_view.xml', 
    ],
    'qweb': [
        'static/src/xml/web_base.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 12,
    'currency': 'EUR',
}
