from flask import Blueprint
from flask import jsonify

basic_blueprint = Blueprint("basic", __name__)


@basic_blueprint.route("/health", methods=["GET"])
def root():
    """Health check endpoint to verify the application is running."""
    return jsonify({"status": "UP", "message": "Service is running!"}), 200
