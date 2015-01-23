import sys

import flask
import flask.ext.basicauth
import flask.ext.sqlalchemy
import flask.ext.bigtempo


import data
import config.env as env
import config.logs as logs


# CONFIGURING LOGGING
logs.default_config()


# INITIALIZING FLASK
# Instance
flask_instance = _flask = flask.Flask(
    __name__,
    static_folder=env.settings('FLASK_STATIC_FOLDER'),
    template_folder=env.settings('FLASK_TEMPLATE_FOLDER'),
    static_url_path=''
)
# Configurations
flask_instance.config.from_object('server.config.flask_commons')
flask_instance.config.from_object(env.settings('FLASK_CONFIG_OBJECT'))


# VALIDATING PRECONDITIONS
# Basic Auth environment variables
if not _flask.config['BASIC_AUTH_USERNAME'] or not _flask.config['BASIC_AUTH_PASSWORD']:
    print ('Setting non-empty BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD '
           'environment variables is mandatory. Exiting...')
    sys.exit()


# INITIALIZING EXTENSIONS AND SERVICES
# Extensions
basic_auth = flask.ext.basicauth.BasicAuth(_flask)
persistence = flask.ext.sqlalchemy.SQLAlchemy(_flask)
datastore = flask.ext.bigtempo.DatastoreAPI(_flask, persistence.engine)


# SETTING THE APPLICATION UP
# Main Routes
@_flask.route('/')
@basic_auth.required
def index():
    return _flask.send_static_file('index.html')
