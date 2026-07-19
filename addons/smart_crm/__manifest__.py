{
    'name': 'Smart CRM + AI Bot',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Universal CRM with real accounting integration and AI bot',
    'author': 'Ismatillo Ismatov',
    'depends': ['base', 'mail', 'account', 'contacts','sale','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/crm_lead_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
} 