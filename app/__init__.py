import logging

from dotenv import load_dotenv
from flask import Flask

from app.database.routes import database_blueprint

load_dotenv()


def create_app():
    """Create Application"""
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.logger.setLevel(10)

    # Register blueprints
    app.register_blueprint(database_blueprint)
    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    create_app().run(debug=True)
