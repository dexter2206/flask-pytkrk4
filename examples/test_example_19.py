"""Test cases for example 19."""
import pytest
from examples.example_19_application_factory import create_app, db
from examples.models import Artist, Album

@pytest.fixture
def app():
    # This database URI specifies sqlite in memory database that will be discarded
    # Once we are done with testing
    app = create_app("sqlite://")
    db.create_all(app=app)
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def populate_db():
    quebonafide = Artist(id=1, name="Quebonafide")
    db.session.add(Album(id=2, title="Romantic Psycho", artist=quebonafide))
    db.session.add(Album(id=1, title="Egzotyka", artist=quebonafide))
    db.session.add(Album(id=3, title="Europa", artist=Artist(id=2, name="Taco Hemingway")))


def test_getting_albums_from_an_empty_database_returns_empty_list(client):
    response = client.get("/albums")
    assert response.status_code == 200
    # Notice the difference between flask test client and requests module!
    # Here json is a property, not a function!
    assert response.json == []


def test_getting_albums_without_title_filter_returns_all_albums(client, app):
    with app.app_context():
        populate_db()

        response = client.get("/albums")

    expected_list = [
        {"id": 1, "title": "Egzotyka", "artist": "Quebonafide"},
        {"id": 2, "title": "Romantic Psycho", "artist": "Quebonafide"},
        {"id": 3, "title": "Europa", "artist": "Taco Hemingway"}
    ]

    actual_list = sorted(response.json, key=lambda album: album["id"])

    assert actual_list == expected_list


def test_filtering_by_title_matches_full_title(client, app):
    with app.app_context():
        populate_db()

        response = client.get("/albums", query_string={"title": "Europa"})

    assert response.json == [{"id": 3, "title": "Europa", "artist": "Taco Hemingway"}]


def test_filtering_by_title_matches_partial_title(client, app):
    with app.app_context():
        populate_db()

        response = client.get("/albums", query_string={"title": "ro"})

    expected_list = [
        {"id": 2, "title": "Romantic Psycho", "artist": "Quebonafide"},
        {"id": 3, "title": "Europa", "artist": "Taco Hemingway"}
    ]

    actual_list = sorted(response.json, key=lambda album: album["id"])

    assert actual_list == expected_list
