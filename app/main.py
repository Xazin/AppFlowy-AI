import logging
import sys
from database.routes import database_blueprint
from basic.routes import basic_blueprint
from dotenv import load_dotenv
from flask import Flask

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 5000

load_dotenv()

app = Flask(__name__)

def main():
    host = str(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PORT

    # TODO: build error
    # logging.basicConfig(level=logging.DEBUG)
    # app.config.from_object("config.settings")
    # app.logger.setLevel(10)

    # Register blueprints
    app.register_blueprint(basic_blueprint)
    app.register_blueprint(database_blueprint)
    app.run(debug=False, host=host, port=port)

if __name__ == '__main__':
    main()
