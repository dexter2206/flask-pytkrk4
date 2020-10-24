from typing import List

from pydantic import BaseModel, StrictStr, StrictInt


class Person(BaseModel):
    first_name: StrictStr
    last_name: str
    age: StrictInt
    numbers: List[int]


if __name__ == '__main__':
    person = Person(
        first_name="Konrad", last_name="Jałowiecki", age=32, numbers=[1,2,3]
    )
    print(person)
