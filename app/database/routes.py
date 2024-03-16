import logging

from flask import Blueprint, jsonify, request

from app.database.summarize import summarize_row
from app.database.translate import translate_row

database_blueprint = Blueprint("database", __name__)


@database_blueprint.route("/translate_row", methods=["POST"])
def translate_row_handler():
    if not request.is_json:
        return jsonify({"error": "Missing payload in request"}), 400

    data = request.get_json()
    if not data:
        raise ValueError("The payload is empty. Please provide a valid row.")

    try:
        response = translate_row(data)
        logging.debug(f"response: {response}")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"data": response})


@database_blueprint.route("/summarize_row", methods=["POST"])
def summarize_row_handler():
    """
    Summarizes table row data from POST requests.

    Accepts POST requests with JSON payloads of table rows, generating and returning a summary. The payload must be in the expected schema.

    Payload:
    - Key-value pairs of table columns and their values.

    Responses:
    - 200 OK: Returns summary.
    - 400 Bad Request: Payload missing or incorrect schema.
    - 500 Internal Server Error: Unexpected error in summarization.

    Returns:
    - JSON response with summary or error message.
    """
    if not request.is_json:
        return jsonify({"error": "Missing payload in request"}), 400

    data = request.get_json()

    if not data:
        raise ValueError("the row is empty. Please provide a valid row.")

    try:
        response = summarize_row(data)
        logging.debug(f"response: {response}")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"data": response})
