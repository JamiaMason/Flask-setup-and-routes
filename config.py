import os

baseddir = os.path.abspath(os.path.dirname(__name__))


class Config():
    FLASK_APP = os.evniron.get('FLASK_APP')
    FLASK_ENV = os.eviron.get("FLASK.ENV")