import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.getenv("FLASK_DEBUG", "true")))

SERVER_NAME = "{host}:{port}".format(
    host=os.getenv("APPFLOWY_AI_SERVER_HOST", "localhost"),
    port=os.getenv("APPFLOWY_AI_SERVER_PORT", "5001"),
)
