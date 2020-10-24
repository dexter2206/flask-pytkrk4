"""Example 19: application factory."""
import pathlib
from typing import Optional

from flask import Flask, request, jsonify
from examples.models import db, Album


# Instead of implementing your app as a global object, implement a factory function
# instead. Arguments to this function can control how the app is instantiated.
# Therefore, you can use different configurations for production/development
# or for testing.
# Usually, the application config is provided but in the below example
# we just pass database_uri
def create_app(database_uri: Optional[str] = None) -> Flask:
    app = Flask(__name__)

    # If database_uri is None, we default to the database we used previously
    if database_uri is None:
        db_file_path = pathlib.Path(__file__).parent.parent / "chinook.db"
        database_uri = f"sqlite:///{db_file_path}"

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    db.init_app(app)

    @app.route("/albums")
    def all_albums():
        query = db.session.query(Album)
        if request.args.get("title"):
            query = query.filter(Album.title.like(f"%{request.args.get('title')}%"))
        return jsonify([album.to_dict() for album in query])

    return app


if __name__ == '__main__':
    create_app().run()
