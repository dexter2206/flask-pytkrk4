# Example 03: debug mode
from flask import Flask

app = Flask(__name__)


@app.route("/")
def broken_route():
    a = 10
    b = 0
    return str(a / b)


if __name__ == "__main__":
    # Setting debug to True turns on debugger and
    # tracking of file changes. This way we gain access
    # to interactive console when things go sideways,
    # and the server will restart itself if any files
    # used for running application change on disk.
    app.run(port=8000, debug=True)
