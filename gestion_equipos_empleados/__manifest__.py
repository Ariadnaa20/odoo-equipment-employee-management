{
    'name': "IT Equipment and Employee Management",
    'version': '16.0',
    'summary': "Manage IT equipment and employee loans",
    'description': "Manage IT devices, loans, employees, and send reports.",
    'author': "Ariadna Pascual",
    'category': 'Asset Management',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/prestamo_mail_wizard_view.xml',
        'wizard/prestamo_report_template.xml',
        'wizard/prestamo_report.xml',
        'views/menu_views.xml',
        'views/equipo_views.xml',
        'views/report_equipo_qr.xml',
        'views/prestamo_views.xml',
        'views/empleado_views.xml',
        'views/busqueda_ia_views.xml',  
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'price': 99.99,
    'currency': 'EUR'

}
