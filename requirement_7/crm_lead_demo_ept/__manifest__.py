{
    'name': 'CRM Demo App',
    'version': '1.0',
    'sequence': -100,
    'summary': 'CRM Demo Software',
    'description': """CRM Demo Software""",
    'depends': ['sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_demo_ept.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
