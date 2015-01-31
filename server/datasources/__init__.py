import os

import bigtempo.core
import flask_bigtempo


store = None
engine = bigtempo.core.DatasourceEngine()


__all__ = []
for module in os.listdir(os.path.dirname(__file__)):
    basename, extension = os.path.splitext(module)
    if module == '__init__.py' or extension.lower() not in ['.py']:
        continue
    __all__.append(basename)
del module


def set_local_store(datastore=None):
    global store
    store = datastore

# TODO: Master: Create add_local_store and add_remote_store which you can register datasources
