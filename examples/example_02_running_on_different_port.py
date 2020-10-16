# Example 02: basic Flask application, this time running on different port
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!!"


if __name__ == "__main__":
    # You can specify the port the application binds to.
    # It is also possible to override the host, but we will leave
    # it s it is for now.
    app.run(port=9000)
