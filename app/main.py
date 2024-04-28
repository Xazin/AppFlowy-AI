import os

from app import create_app

if __name__ == "__main__":
    host = os.environ.get("APPFLOWY_AI_HOST", "localhost")
    port = os.environ.get("APPFLOWY_AI_PORT", "5001")
    create_app().run(debug=False, host=host, port=port)
