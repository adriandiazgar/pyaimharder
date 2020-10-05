# -*- coding: utf-8 -*-

'''
Settings and stuff.
'''

import os

DEBUG = bool(os.environ.get(('DEBUG'), False))
if DEBUG:
    BASE_URL = 'https://localhost'
else:
    BASE_URL = 'https://aimharder.com'

# TODO: add list of boxes as needed
BOXES = {
    'castelldefels': {
        'id': 9283,
        'BASE_URL': 'https://crossfitboxcastelldefels.aimharder.com'
    }
}

LOGIN = ''
BOOK = ''
BOX_ID = ''
CLASSES = ''

def set_box(name):
    global BOOK
    global BOX_ID
    global LOGIN
    global  CLASSES

    BASE_URL = BOXES[name]['BASE_URL']
    BASE_API_URL = '{}/{}'.format(BASE_URL, 'api')
    CLASSES = '{}/{}'.format(BASE_API_URL, 'bookings')
    LOGIN = '{}/{}'.format(BASE_URL, 'login')
    BOX_ID = BOXES[name]['id']
    BASE_API_URL = '{}/{}'.format(BASE_URL, 'api')
    BOOK = '{}/{}'.format(BASE_API_URL, 'book')
