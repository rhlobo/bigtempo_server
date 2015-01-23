#!/usr/bin/env python


import sh
import sys
import flask.ext.script

import server.app as server
import wsgi


instance = server.flask_instance
manager = flask.ext.script.Manager(instance)


@manager.command
def run():
    wsgi.run()


if __name__ == '__main__':
    manager.run()
