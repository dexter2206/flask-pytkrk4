"""App combining genres and albums blueprints."""
import pathlib

from flask import Flask

from examples.models import db
from solutions.solution_06_db_and_blueprints.genres import genres
from solutions.solution_06_db_and_blueprints.albums import albums

app = Flask(__name__)

DB_FILE_PATH = pathlib.Path(__file__).parent.parent.parent / "chinook.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
db.init_app(app)


app.register_blueprint(genres, url_prefix="/genres")
app.register_blueprint(albums, url_prefix="/albums")

if __name__ == '__main__':
    app.run()
