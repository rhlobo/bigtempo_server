import flask
import flask.ext.basicauth
import flask.ext.sqlalchemy
import flask.ext.restless
import flask.ext.bigtempo
import flask.ext.session

import config.env as env
import config.logs as logs

import auth
import datasources


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
auth.validate_preconditions(_flask)


# INITIALIZING EXTENSIONS AND SERVICES
# Flask Extensions
session_mngr = flask.ext.session.Session(_flask)
basic_auth = flask.ext.basicauth.BasicAuth(_flask)
persistence = flask.ext.sqlalchemy.SQLAlchemy(_flask)
restless_webapis = flask.ext.restless.APIManager(_flask, flask_sqlalchemy_db=persistence)
datastore_webapi = flask.ext.bigtempo.DatastoreAPI(_flask, persistence.engine)
bigtempo_webapi = flask.ext.bigtempo.BigtempoAPI(_flask, datasources.engine)


# SETTING THE APPLICATION UP
# Main Routes
@_flask.route('/')
@basic_auth.required
def index():
    return _flask.send_static_file('index.html')

# Bigtempo datasources
(bigtempo_webapi.create_datasource_factory(datastore_webapi)
    .register('LOCAL_DATA_SOURCE1')
    .register('LOCAL_DATA_SOURCE2'))
(bigtempo_webapi.create_datasource_factory('http://remotehost:5000')
    .register('REMOTE_DATA_SOURCE1'))

from datasources import *

# Domain modules
from domain import *

# Database tables
persistence.create_all()
