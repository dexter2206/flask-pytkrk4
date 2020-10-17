"""Example 12: using for loop in templates."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.jinja2", title="Strona główna")


@app.route("/subpage")
def subpage():
    return render_template("subpage.jinja2", title="Podstrona")


if __name__ == '__main__':
    app.run()
