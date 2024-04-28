from flask import Blueprint, jsonify

basic_blueprint = Blueprint("basic", __name__)


@basic_blueprint.route("/health", methods=["GET"])
def root():
    """Health check endpoint to verify the application is running."""
    return jsonify({"status": "UP", "message": "Service is running!"}), 200
