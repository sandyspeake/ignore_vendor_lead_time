# -*- coding: utf-8 -*-
{
    "name": "Ignore Vendor Lead Times",
    "summary": """Do not consider Vendor Lead Time for Replenishment""",
    "description": 
    """
    This module removes the consideration of Vendor Lead Times from the Replenish Rules. 
    """,
    "author": "Sanford Speake",
    "category": "stock",
    "version": "15.0.1.0.0",
    "depends": ["base","stock"],
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    'auto_install': False,
    'price': 30.00,
    'currency': 'USD',
    "data": [
        "views/res_config_settings_views.xml",
    ],
}