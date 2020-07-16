"""Flask config."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    """Base config."""
    SECRET_KEY = 'BASE_KEY'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = r'sqlite:///' + path.join(basedir, 'db/db.sqlite')
    SESSION_COOKIE_NAME = environ.get('SESSION_PROD_COOKIE')


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = r'sqlite:///' + path.join(basedir, 'db/db.sqlite')
    SESSION_COOKIE_NAME = 'DEV_COOKIE'
