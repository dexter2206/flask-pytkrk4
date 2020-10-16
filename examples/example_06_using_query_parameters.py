# Example 06: Using query arguments.
from flask import Flask, request


app = Flask(__name__)


@app.route("/hello")
def hello():
    # request.args is a mapping containing passed query arguments.
    # It behaves like a dictionary - be aware of possible BadRequestKeyErrors!
    name = request.args["name"]
    return f"Hello, {name}!"


@app.route("/hello-with-default")
def hello_2():
    # As with a dict, you can use get method and pass additional default value.
    name = request.args.get("name", "World")
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run()
