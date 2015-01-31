import sys

import config.env as env


def validate_preconditions(app):
    if not env.is_production():
        return

    username = app.config['BASIC_AUTH_USERNAME']
    password = app.config['BASIC_AUTH_PASSWORD']

    if not username or not password:
        print ('Setting non-empty BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD '
               'environment variables is mandatory. Exiting...')
        sys.exit()
