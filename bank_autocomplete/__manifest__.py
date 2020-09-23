{
    'name': "Bank Autocomplete",
    'version': '1.0.0',
    'summary': 'Auto-complete bank data ',
    'depends': ['base'],
    'author': "Sébastien Mottet",
    'license': "OPL-1",
    'category': 'Accounting',
    'description': """
        More than 100k pre-encoded banks.
    """,
    'images': ['static/description/banner.png'],
    'support': 'sebastien.mottet96@gmail.com',
    'price': 5.0,
    'currency': 'EUR',
    'installable': True,
    'post_init_hook': '_populate_res_bank',
}