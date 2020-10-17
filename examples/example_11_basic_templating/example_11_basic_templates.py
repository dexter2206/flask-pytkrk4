"""Example 11: basic use of templates."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.jinja2",
        title="Hello World App",
        welcome_message="Welcome to my first application with template!"
    )


if __name__ == '__main__':
    app.run()
