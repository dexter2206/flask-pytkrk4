import pytest
from .example_01_hello_world import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root_endpoint_returns_hello_world_response_with_200_ok(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
