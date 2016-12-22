# coding: utf-8

{
    'name': 'Convert CRM Claim to CR',
    'version': '8.0.1.0.0',
    'author':   'Simbioz ',
    'contributors': [
        
    ],
    'website': 'http://simbioz.com.ua',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'summary': '''Convert a crm claim to a Change Request''',
    'depends': [
        'base',
        'crm_claim',
        'change_management'
    ],
    'demo': [],
    'data': [
        'wizard/convert_claim_view.xml',
        'view/claim_view.xml'
    ],
    'test': [],
    'js': [],
    'css': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
