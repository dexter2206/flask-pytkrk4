"""Blueprint for users."""
from flask import Blueprint, render_template

users = Blueprint("users", __name__)

USERS = [
    {"login": "ak74", "email": "anna.kowalska@gmail.com"},
    {"login": "dexter", "email": "dexter2206@gmail.com"},
    {"login": "konrad", "email": "konrad.jalowiecki@smcebi.edu.pl"}
]


# This will be available at <prefix>/, where prefix is chosen when registering
# the blueprint.
@users.route("/")
def all_users():
    return render_template("users.jinja2", users=USERS)

