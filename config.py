"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
env_path = path.join(path.dirname(__file__), '.env')

class Config:
    """Base config.""" 
    load_dotenv(env_path)
    DEBUG = environ.get("DEBUG")
    ENV = environ.get("FLASK_ENV")
    FLASK_ENV = environ.get("FLASK_ENV")
    TESTING = environ.get("TESTING")
    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    
    SQLALCHEMY_DATABASE_URI = r'sqlite:///' + path.join(basedir, 'golinks/db/db.sqlite')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
