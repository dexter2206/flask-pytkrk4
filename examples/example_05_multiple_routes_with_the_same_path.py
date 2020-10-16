# Example 05: multiple routes with the same path
from flask import Flask, request

app = Flask(__name__)


# You can specify the route with the same path but using different methods.
# This allows you to separate behaviour of given route without putting
# too much conditional logic in its implementation.
@app.route("/hello", methods=["GET"])
def hello_get():
    return "Hello called with GET method."


@app.route("/hello", methods=["POST"])
def hello_post():
    return "Hello called with POST method."


if __name__ == "__main__":
    app.run()
