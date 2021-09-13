{
    'name': 'Employee EPT',
    'version': '1.0',
    'sequence': -100,
    'summary': 'Employee EPT Software',
    'description': """Employee EPT Software""",
    'depends': ['base'],
    'data': [
        'security/security_crm_group.xml',
        'security/ir.model.access.csv',
        'views/employee_ept.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
