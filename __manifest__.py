{
    'name': "Gestió d'Equips i Empleats",
    'version': '1.0',
    'summary': "Gestió d'equips informàtics i préstecs a empleats",
    'description': "Gestió d'equips, préstecs, empleats i enviament d'informes.",
    'author': "Ariadna Pascual",
    'category': 'Tools',
    'license': 'OPL-1',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/prestamo_mail_wizard_view.xml',
        'wizard/prestamo_report_template.xml',
        'wizard/prestamo_report.xml',
        'views/menu_views.xml',
        'views/equipo_views.xml',
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
}
