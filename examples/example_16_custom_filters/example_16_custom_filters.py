"""Example 15: basic filters."""
from flask import Flask, render_template

app = Flask(__name__)

CARD_NUMBERS = [
    "6762206565953351",
    "5038155342846760",
    "5018296210062660"
]


@app.route("/")
def cards():
    return render_template(
        "custom_filters.jinja2",
        card_numbers=CARD_NUMBERS
    )


@app.template_filter()
def hide_card_number(number):
    # This assumes card numbers composed of 16 digits
    return f"**** **** **** {number[-4:]}"


if __name__ == '__main__':
    app.run()
