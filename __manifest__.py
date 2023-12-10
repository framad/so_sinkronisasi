# -*- coding: utf-8 -*-
{
    'name': "SO Sinkronisasi",

    'summary': """
        SO Sinkronisasi""",

    'description': """
       SO Sinkronisasi
    """,

    'author': "Febry",
    'website': "framad.github.io/framadhan",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['base','sale'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        # 'views/sale_order_custom_view.xml',
        'views/menuteims.views.xml',
        'views/sales_order_clone.views.xml',
        # 'views/rekapsol.views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}