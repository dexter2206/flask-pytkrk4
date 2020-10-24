"""App combining genres and albums blueprints."""
import pathlib
from typing import Optional

from flask import Flask

from examples.models import db
from solutions.solution_08_db_and_blueprints.genres import genres
from solutions.solution_08_db_and_blueprints.albums import albums


def create_app(database_uri: Optional[str] = None) -> Flask:
    app = Flask(__name__)

    if database_uri is None:
        db_file_path = pathlib.Path(__file__).parent.parent.parent / "chinook.db"
        database_uri = f"sqlite:///{db_file_path}"

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    db.init_app(app)

    app.register_blueprint(genres, url_prefix="/genres/")
    app.register_blueprint(albums, url_prefix="/albums/")

    return app


if __name__ == '__main__':
    create_app().run()
