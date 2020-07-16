"""Initialize Flask Application."""
from flask import Flask
from golinks.models import DB
import os


def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///' + os.path.join(os.path.dirname(os.path.realpath(__file__)), 'db\db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'CHANGE_ME'
    app.debug = False
    DB.init_app(app)
    
    print(os.path.dirname(os.path.realpath(__file__)))
    with app.app_context():
        from . import routes

        DB.create_all()

        return app