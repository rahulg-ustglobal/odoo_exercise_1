{
        'name': 'Country Demo',
        'version': '1.0',
        'sequence': -100,
        'summary': 'Country Demo Software',
        'description': """Country Demo Software""",
        'depends': ['sales_team'],
        'data' :[
        'security/ir.model.access.csv',
        'views/res_country_ept.xml'
    ],
    'demo' :[
    ],
        'installable': True,
        'application': True,
        'auto_install': False,
    }

