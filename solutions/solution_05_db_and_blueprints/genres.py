"""Blueprint with operations on genre model."""
from flask import Blueprint, jsonify, request

from examples.models import Genre, db

genres = Blueprint("genres", __name__)


@genres.route("/", methods=["GET"])
def get_all_genres():
    response = jsonify([genre.to_dict() for genre in db.session.query(Genre)])
    return response


# Resource for posting departments.
@genres.route("/", methods=["POST"])
def add_genre():
    data = request.get_json()
    try:
        genre = Genre(name=data["name"])
        db.session.add(genre)
        db.session.commit()
        return jsonify(genre.to_dict())
    except KeyError:
        response = jsonify({"error": "Bad request", "missing field": "name"})
        response.status_code = 400
        return response


# Resource for getting given genre
@genres.route("/<int:genre_id>", methods=["GET"])
def get_genre(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    return jsonify(genre.to_dict())


# Resource for patching genre, i.e. modifying part of the object.
@genres.route("/<int:genre_id>", methods=["PATCH"])
def patch_genre(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    genre.name = request.get_json().get("name", genre.name)
    db.session.add(genre)
    db.session.commit()
    return jsonify(genre.to_dict())


# Resource for deleting genre
@genres.route("/<int:genre_id>", methods=["DELETE"])
def delete_genre(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    db.session.delete(genre)
    db.session.commit()
    return jsonify("")
