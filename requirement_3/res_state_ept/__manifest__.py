{
        'name': 'State Demo',
        'version': '1.0',
        'sequence': -100,
        'summary': 'State Demo Software',
        'description': """State Demo Software""",
        'depends': ['sales_team'],
        'data' :[
            'security/ir.model.access.csv',
            'views/res_state_demo_ept.xml'
    ],
    'demo' :[
    ],
        'installable': True,
        'application': True,
        'auto_install': False,
    }

