"""Test cases for example 19."""
import pytest
from solutions.solution_08_db_and_blueprints.solution_08 import create_app, db


@pytest.fixture
def app():
    app = create_app("sqlite://")
    db.create_all(app=app)
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_posted_genre_can_be_retrieved_by_its_id(client, app):
    # Step 1: Post new genre
    # Step 2: Obtain id from the response
    # Step 3: Get genre with given id
    # Step 4: check if response has correct status code
    # Step 5: check if name of the genre is correct
    response = client.post("/genres/", json={"name": "Rock"})

    genre_id = response.json["id"]
    response = client.get(f"/genres/{genre_id}/")

    assert response.status_code == 200
    assert response.json["name"] == "Rock"
