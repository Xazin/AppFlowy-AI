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
        resp = translate_row(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"response": resp})


@database_blueprint.route("/summarize_row", methods=["POST"])
def summarize_row_handler():
    """
    Handle requests to summarize table row data.

    This route accepts POST requests with JSON payloads representing a single row from a table. The row data is then
    processed to generate a summary. The function expects the payload to match the expected schema for summarization
    and returns a JSON response with the summary or an error message.

    Payload Structure:
    The JSON payload should contain key-value pairs corresponding to the columns and their values in the row to be
    summarized.

    Responses:
    - 200 OK: The request was successful, and the response body contains the summarized data.
    - 400 Bad Request: The request was malformed, either because the payload was missing or the data did not meet
      the expected schema.
    - 500 Internal Server Error: An unexpected error occurred during the summarization process.

    Returns:
        A Flask response object with a JSON body. The body contains either the summary under the "response" key for
        successful requests or an error message under the "error" key for failed requests.
    """

    if not request.is_json:
        return jsonify({"error": "Missing payload in request"}), 400

    data = request.get_json()

    if not data:
        raise ValueError("the row is empty. Please provide a valid row.")

    try:
        resp = summarize_row(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify({"response": resp})
