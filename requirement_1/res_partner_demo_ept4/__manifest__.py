{
    'name' : 'Contacts 4',
    'version' : '1.0',
    'sequence' : -100,
    'summary' : 'Partner Demo Software',
    'description' : """Partner Demo Software""",
    'depends' :['sales_team'],
    'data' :[
        'security/ir.model.access.csv',
        'views/res_partner_demo_ept4.xml'
    ],
    'demo' :[
        'data/demo_data_res_partner_ept4.xml'
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}

