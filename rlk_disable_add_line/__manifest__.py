{
    'name': 'Hide Add a Line when Not Draft',
    'version': '17.0.1.0',
    'summary': 'Hides the "Add a Line" option when record state is not draft, while keeping edit enabled if not readonly.',
    'description': """
        This module customizes one2many list views so that the "Add a line" button 
        is hidden when the parent record state is not 'draft'. 
        Editing existing lines is still allowed unless the field is readonly. 
        Works across all models using a `state` field.
    """,
    'author': "ryanlinnok",
    'website': 'https://ryanlinnok.github.io',
    'license': 'LGPL-3',
    'category': 'Web',
    'depends': [
        'web',  
    ],
    'assets': {
        'web.assets_backend': [
            'rlk_disable_add_line/static/src/js/hide_add_line.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
