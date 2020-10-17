"""Example 12: using for loop in templates."""
from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name": "X1 Carbon Laptop", "manufacturer": "Lenovo", "price": 9906},
    {"name": "iMac Pro 32 GB", "manufacturer": "Apple", "price": 10739},
    {"name": "Galaxy S10", "manufacturer": "Samsung", "price": 2999}
]


@app.route("/products", methods=["GET"])
def products():
    return render_template("products.jinja2", products=PRODUCTS)


if __name__ == '__main__':
    app.run()
