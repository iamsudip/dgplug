#!/usr/bin/env python

import flask

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/log/<log_id>/')
def log(log_id):
    """ Displays the page greats who ever comes to visit it.
    """
    return flask.render_template('log.html', name=log_id)

if __name__ == '__main__':
    port = 8000
    APP.debug=True
    APP.run(port = port)


