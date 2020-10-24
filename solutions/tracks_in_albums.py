# Example 17: using Flask with SQLAlchemy
import pathlib
from flask import Flask, request, jsonify, render_template

# Import relevant model and engine.
from examples.models import db, Album

app = Flask(__name__)

# During classes, my DB file will reside here
DB_FILE_PATH = pathlib.Path(__file__).parent.parent / "chinook.db"


# For the engine to work we need to configure database URI
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"

# And initialize it with an app
db.init_app(app)


@app.route("/album/<int:album_id>")
def albums_details(album_id):
    album = Album.query.filter_by(id=album_id).first_or_404()
    return render_template("album_details.jinja2", album=album)


if __name__ == '__main__':
    app.run()
