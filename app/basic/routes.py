from flask import Blueprint, Response;

basic_blueprint = Blueprint("basic", __name__)

# use to ping the server
@basic_blueprint.route("/")
def root():
    return Response("Server is running", status=200)
