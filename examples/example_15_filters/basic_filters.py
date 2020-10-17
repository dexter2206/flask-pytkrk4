"""Example 15: basic filters."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def basic_filters():
    return render_template(
        "filters.jinja2",
        numbers=[1, -2, 4, 0, 3, 1],
        string="The quick brown fox jumped over a lazy dog"
    )


if __name__ == '__main__':
    app.run()
