# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Web Translate",
    'summary': "Web Translate Indonesian",
    'author': "tono.awar@gmail.com",
    'version': '1.1',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'web_translate/static/src/xml/calendar_controller.xml',
            'web_translate/static/src/xml/hierarchy_controller.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}