from database.routes import database_blueprint
from dotenv import load_dotenv
from flask import Flask

from app.config import DevelopmentConfig

# Load .env file
load_dotenv()


def create_app(config_object=DevelopmentConfig):
    """Create Application"""
    app = Flask(__name__)
    app.config.from_object(config_object)

    # CRITICAL = 50
    # ERROR = 40
    # WARNING = 30
    # INFO = 20
    # DEBUG = 10
    app.logger.setLevel(10)

    # Register blueprints
    app.register_blueprint(database_blueprint)
    return app
