#
# Flask-Keen
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


import logging

from keen.client import KeenClient


logger = logging.getLogger('Flask-Keen')


class Keen(object):
    """
    Flask-Keen

    Documentation:
    https://flask-keen.readthedocs.io

    API:
    https://keen.io/docs

    :param app: Flask app to initialize with. Defaults to `None`
    """

    client = None

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        project_id = app.config.get('KEEN_PROJECT_ID')
        if project_id is None:
            logger.warning('KEEN_PROJECT_ID not set')
            return
        self.client = KeenClient(
            project_id=project_id,
            write_key=app.config.get('KEEN_WRITE_KEY'),
            read_key=app.config.get('KEEN_READ_KEY'),
        )

    def __getattr__(self, name):
        return getattr(self.client, name)


# EOF
