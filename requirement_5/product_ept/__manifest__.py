{
        'name': 'Product',
        'version': '1.0',
        'sequence': -100,
        'summary': 'Product Software',
        'description': """Product Software""",
        'depends': ['sales_team'],
        'data' :[
            'security/ir.model.access.csv',
            'views/product_ept.xml'
    ],
    'demo' :[
    ],
        'installable': True,
        'application': True,
        'auto_install': False,
    }

