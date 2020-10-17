# Example 10: using json with flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/incoming-json", methods=["POST"])
def post_json():
    # If content type of the request is application/json, Flask can
    # automatically decode json object for you.
    # Remember, this will only work if the correct content type is set in the request.
    # Alternatively, you can forcefuly interpret incoming data as json by passing
    # force=True to request.get_json()
    return "\n".join(f"{key}: {value}" for key, value in request.get_json().items())


@app.route("/outgoing-json", methods=["GET"])
def get_json():
    # jsonify works like a json.dumps function. but wraps the encoded
    # json in a response object
    response = jsonify({"foo": 2, "bar": 3})
    return response


if __name__ == '__main__':
    app.run()
