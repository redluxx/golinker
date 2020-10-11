"""Initialize Flask Application."""
from flask import Flask
from golinks.models import DB, Settings

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')
    DB.init_app(app)
  
    with app.app_context():
        from . import views
        from .extras.settings import views

        DB.create_all()
        Settings.setup()

        return app