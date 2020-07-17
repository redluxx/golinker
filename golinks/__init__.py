"""Initialize Flask Application."""
from flask import Flask
from golinks.models import DB

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')
    DB.init_app(app)
  
    with app.app_context():
        from . import routes

        DB.create_all()

        return app