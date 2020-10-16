# Example 07: using path parameters.
from flask import Flask

app = Flask(__name__)


# Routes can have parameterized paths. Parameters are denoted with
# angular brackets <>. Concrete values, with which resource has been
# accessed, is passed as a keyword argument with the same name.
@app.route("/hello/<name>")
def hello_with_path_param(name):
    return f"Hello, {name}!"


# You can specify the converter to use for given path parameter.
# In this way, the parameter will be automatically checked and
# the argument passed to the function itself will always have
# the expected type. Note that values of the parameter that
# don't match the expected types will be ignored, resulting in
# 404 error.
@app.route("/increment/integer/<int:x>")
def integer(x):
    return f"You int incremented by one: {x+1}"


# You can have multiple path parameters in the same route.
@app.route("/<greeting>/<name>")
def greeting_with_path_param(greeting, name):
    return f"{greeting.title()}, {name}!"


if __name__ == "__main__":
    app.run()
