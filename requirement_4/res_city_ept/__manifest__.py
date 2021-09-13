{
        'name': 'City Demo',
        'version': '1.0',
        'sequence': -100,
        'summary': 'City Demo Software',
        'description': """City Demo Software""",
        'depends': ['sales_team'],
        'data' :[
            'security/ir.model.access.csv',
            'views/res_city_ept.xml'
    ],
    'demo' :[
    ],
        'installable': True,
        'application': True,
        'auto_install': False,
    }

