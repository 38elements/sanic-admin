import sys
import os
import json
import sanic_admin.reload
import sanic_admin.urls


def run():
    SETTING_FILE_NAME = 'sanic-admin.json'
    setting_file = None
    setting = {
        'paths': [os.getcwd()],
        'patterns': ['*.py'],
        'before': None,
        'before_each': None,
        'after': None,
        'after_each': None,
        'app': 'app'
    }

    try:
        setting_file = open(SETTING_FILE_NAME, 'r')
    except:
        pass

    if setting_file:
        _setting = json.load(setting_file)
        setting_file.close()
        for key in setting.keys():
            if key in _setting:
                setting[key] = _setting[key]

    if '-urls' in sys.argv:
        sanic_admin.urls.run(setting)
    else:
        sanic_admin.reload.run(setting)
