# Example 09: different objects that can be used as a response.
from flask import Flask, make_response

app = Flask(__name__)


# Option 1: tuple of the form (content, headers)
@app.route("/tuple", methods=["GET"])
def resp_from_tuple():
    return "Response returned as a tuple", {"MyCustomHeader": 21}


# Option 2: tuple of the form (content, status code, headers)
@app.route("/triple", methods=["GET"])
def resp_from_triple():
    return 'Response returned as a "triple"', 417, {"MyCustomHeader": 37}


# Option 3.: Response object. You can get one by calling make_response
# on your content and then filling necessary attributes.
@app.route("/response", methods=["GET"])
def resp_obj1():
    resp = make_response("Response returned as a Response object")
    resp.content_type = "application/json"
    resp.status_code = 301
    return resp


if __name__ == '__main__':
    app.run()
