# Example 17: using Flask with SQLAlchemy
import pathlib
from flask import Flask, request, jsonify


# Import relevant model and engine.
from examples.models import db, Genre

app = Flask(__name__)

# During classes, my DB file will reside here
DB_FILE_PATH = pathlib.Path(__file__).parent.parent.parent / "chinook.db"


# For the engine to work we need to configure database URI
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"

# And initialize it with an app
db.init_app(app)


@app.route("/genres", methods=["GET"])
def get_all_genres():
    response = jsonify([genre.to_dict() for genre in db.session.query(Genre)])
    return response


# Resource for posting departments.
@app.route("/genres", methods=["POST"])
def add_genre():
    # Get data
    data = request.get_json()
    # We don't implement sophisticated validation (we will do so with Pydantic later).
    # Here we only catch an exception (raised when name is not present) and return
    # 400 Bad Request in an exception is catched.
    try:
        genre = Genre(name=data["name"])
        db.session.add(genre)
        db.session.commit()
        # Remember that jsonify can't process Model instances. That's why we convert
        # it to dict.
        return jsonify(genre.to_dict())
    except KeyError:
        # Even in case of error we return JSON encoded response.
        response = jsonify({"error": "Bad request", "missing field": "name"})
        response.status_code = 400
        return response


# Resource for getting given genre
@app.route("/genres/<int:genre_id>", methods=["GET"])
def get_genre(genre_id):
    # Query is done as usual with SQLAlchemy.
    # The only difference is that query sets now have (...)_or_404 methods
    # that terminate execution if query is empty.
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    return jsonify(genre.to_dict())


# Resource for patching genre, i.e. modifying part of the object.
@app.route("/genres/<int:genre_id>", methods=["PATCH"])
def patch_genre(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    # Note: usually when patching, full object is not required.
    # Therefore even an empty request is technically correct.
    # We cannot assume that 'name' is in the requests's data
    # nor throw an error in this case.
    genre.name = request.get_json().get("name", genre.name)
    db.session.add(genre)
    db.session.commit()
    return jsonify(genre.to_dict())


# Resource for deleting genre
@app.route("/genres/<int:genre_id>", methods=["DELETE"])
def delete_genre(genre_id):
    genre = db.session.query(Genre).filter_by(id=genre_id).first_or_404()
    db.session.delete(genre)
    db.session.commit()
    return jsonify("")


# An error handler for 404 not found
# We implement it because by default HTML page with error is returned -
# we want JSON response instead.
@app.errorhandler(404)
def handle_404(error):
    response = jsonify({"error": 404, "text": str(error)})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()
