# This assumes example_17 is running
import requests

ADDRESS = "http://localhost:5000"
ENDPOINT = ADDRESS + "/genres"

if __name__ == '__main__':
    # Getting all genres from DB
    get_response = requests.get(ENDPOINT)
    print("all genres", get_response.json())

    # Posting new genre
    post_response = requests.post(
        ENDPOINT,
        json={"name": "Matematyczny metal"}
    )

    print("The genre you added: ", post_response.json())

    # Modyfing genre
    genre_id = post_response.json()["id"]

    patch_response = requests.patch(
        ENDPOINT + f"/{genre_id}",
        json={"name": "Mathematical metal"}
    )

    print("The genre after modification: ", patch_response.json())

    # Deleting genre we added

    delete_response = requests.delete(
        ENDPOINT + f"/{genre_id}",
    )

    print("Deleted successfuly?", delete_response.ok)
