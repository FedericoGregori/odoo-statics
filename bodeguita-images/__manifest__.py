# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Bodeguita Images Module',
    'summary': """
        This module is used to handle images of Bodeguita Company.""",

    'author': 'Federico Gregori',
    'maintainers': ['FedericoGregori'],

    'website': 'https://www.federicogregori.com.ar/',
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '13.0.1.0.0',
    # see https://odoo-community.org/page/development-status
    'development_status': 'Production/Stable',

    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # 'data': [
    #     'security/ir.model.access.csv',
    #     'views/views.xml',
    #     'views/templates.xml',
    # ],

    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
