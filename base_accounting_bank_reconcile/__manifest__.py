# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Odoo 15 Full Accounting Kit',
    'version': '15.0.2.2.4',
    'category': 'Accounting',
    'live_test_url': 'https://www.youtube.com/watch?v=peAp2Tx_XIs',
    'summary': """Bank reconciliation widget""",
    'description': """
                    Reconciliation Widget,
                    Reconciliation Widget For Odoo15,
                    Payments Matching
                    """,
    'author': 'Cybrosys Techno Solutions, Odoo SA',
    'website': "https://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'account', 'sale', 'account_check_printing', 'base_account_budget'],
    'data': [
        'views/payment_matching.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'base_accounting_bank_reconcile/static/src/scss/style.scss',
            'base_accounting_bank_reconcile/static/lib/bootstrap-toggle-master/css/bootstrap-toggle.min.css',
            'base_accounting_bank_reconcile/static/src/js/payment_model.js',
            'base_accounting_bank_reconcile/static/src/js/payment_render.js',
            'base_accounting_bank_reconcile/static/src/js/payment_matching.js',
            'base_accounting_bank_reconcile/static/lib/bootstrap-toggle-master/js/bootstrap-toggle.min.js',

        ],
        'web.assets_qweb': [
            'base_accounting_bank_reconcile/static/src/xml/template.xml',
            'base_accounting_bank_reconcile/static/src/xml/payment_matching.xml',
        ],
    },
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
