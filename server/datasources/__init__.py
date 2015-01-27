import os

import bigtempo.core
import flask_bigtempo


store = None
engine = bigtempo.core.DatasourceEngine()


__all__ = []


def load(datastore=None):
    global store
    store = datastore

    for module in os.listdir(os.path.dirname(__file__)):
        basename, extension = os.path.splitext(module)
        if module == '__init__.py' or extension.lower() not in ['.py']:
            continue
        __all__.append(basename)
