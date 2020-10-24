"""Example 11: using pydantic for data validation."""
from flask import Flask, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

app = Flask(__name__)


class Operands(BaseModel):
    arg1: float
    arg2: float


class DivQueryArgs(BaseModel):
    truediv: str = "true"


@app.route("/add", methods=["POST"])
@validate()
def add(body: Operands):
    return jsonify(
        {
            "arg1": body.arg1,
            "arg2": body.arg2,
            "operator": "+",
            "result": body.arg1 + body.arg2,
        }
    )


@app.route("/div", methods=["POST"])
@validate()
def div(body: Operands, query: DivQueryArgs):
    try:
        if query.truediv == "true":
            operator, result = "/", body.arg1 / body.arg2
        else:
            operator, result = "//", body.arg1 // body.arg2
        return jsonify(
            {
                "arg1": body.arg1,
                "arg2": body.arg2,
                "operator": operator,
                "result": result
            }
        )
    except ZeroDivisionError:
        response = jsonify({"error": "Zero division error"})
        response.status_code = 400
        return response


if __name__ == "__main__":
    app.run()
