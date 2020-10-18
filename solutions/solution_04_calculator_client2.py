"""Client for our calculator API."""
import requests

API_ADDRESS = "http://localhost:5000"


class CalculatorClient:

    def __init__(self, url):
        self.url = url

    def add(self, arg1: float, arg2: float) -> float:
        return self._compute(arg1, arg2, "/add")

    def sub(self, arg1: float, arg2: float) -> float:
        return self._compute(arg1, arg2, "/sub")

    def square(self, arg1: float) -> float:
        return self._compute(arg1, arg1, "/mul")

    def _compute(self, arg1: float, arg2: float, path: str) -> float:
        response = requests.post(self.url + path, json={"arg1": arg1, "arg2": arg2})
        return response.json()["result"]


if __name__ == '__main__':
    arg1 = float(input("Podaj pierwszy argument: "))
    arg2 = float(input("Podaj drugi argument: "))
    operation = input("Podaj operację: ")

    client = CalculatorClient(API_ADDRESS)

    if operation == "add":
        result = client.add(arg1, arg2)
    elif operation == "sub":
        result = client.sub(arg1, arg2)
    else:
        print(f"Nieznana operacja {operation}")
        exit(1)

    print(f"Wynik: {result}")
