from app.database.routes import database_blueprint
from dotenv import load_dotenv
from flask import Flask

from app.extensions import debug_toolbar

load_dotenv()


def create_app():
    """Create Application"""
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.logger.setLevel(10)

    # Register blueprints
    app.register_blueprint(database_blueprint)
    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    return None


if __name__ == "__main__":
    create_app().run()
