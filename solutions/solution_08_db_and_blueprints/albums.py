"""Blueprint with operations on albums model."""
from flask import Blueprint, jsonify
from examples.models import db, Album

albums = Blueprint("albums", __name__)


@albums.route("/", methods=["GET"])
def get_all_albums():
    return jsonify([album.to_dict() for album in db.session.query(Album)])
