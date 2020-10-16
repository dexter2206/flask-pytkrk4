# Example 04: specifying routes and restricting allowed methods.
from flask import Flask, request

app = Flask(__name__)


# Adding list of methods in @app.route results in restricting given
# route. For other methods, 405 "not allowed" status page will be
# generated.
@app.route("/get_and_post", methods=["GET", "POST"])
def example_get_and_post():
    # The "request" object always holds information associated with the current
    # request. In particular it contains the path and HTTP method.
    return f"{request.path} requested with {request.method} method."


@app.route("/get", methods=["GET"])
def example_get():
    return f"{request.path} requested with {request.method} method."


@app.route("/post", methods=["POST"])
def example_post():
    return f"{request.path} requested with {request.method} method."


if __name__ == "__main__":
    app.run()
