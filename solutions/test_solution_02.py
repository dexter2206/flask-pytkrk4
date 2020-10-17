import pytest

from solutions.solution_02_flask_calculator import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# test_adding_two_numbers
# test_adding
# test_number_addition
# test_01 <- tak nie róbcie
# test_add_5_10
@pytest.mark.parametrize(
    "arg1, arg2, expected_result",
    [
        (5, 13, b"18"),
        (3, 4, b"7"),
        (0, 10, b"10"),
        (5, 8, b"13")
    ]
)
def test_sending_get_request_to_add_endpoint_gives_correct_sum_of_integers(
    client, arg1, arg2, expected_result
):
    response = client.get(f"/add/{arg1}/{arg2}")
    assert response.status_code == 200
    assert response.data == expected_result
