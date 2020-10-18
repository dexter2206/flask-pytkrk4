"""Client for our calculator API."""
import requests

API_ADDRESS = "http://localhost:5000"

ENDPOINTS = {
    "dodaj": "/add",
    "odejmij": "/sub"
}


if __name__ == '__main__':
    arg1 = float(input("Podaj pierwszy argument: "))
    arg2 = float(input("Podaj drugi argument: "))
    operation = input("Podaj operację: ")

    url = API_ADDRESS + ENDPOINTS[operation]
    response = requests.post(url, json={"arg1": arg1, "arg2": arg2})

    if response.status_code != 200:
        print("Problem z działaniem z API.")
        exit(1)

    result = response.json()
    print(
        f"{result['arg1']} {result['operator']} {result['arg2']} = {result['result']}"
    )

