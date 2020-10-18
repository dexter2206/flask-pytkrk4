from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    input_data = request.get_json()
    return jsonify(
        {
            "arg1": input_data["arg1"],
            "arg2": input_data["arg2"],
            "operator": "+",
            "result": input_data["arg1"] + input_data["arg2"]
        }
    )


@app.route("/sub", methods=["POST"])
def sub():
    input_data = request.get_json()
    return jsonify(
        {
            "arg1": input_data["arg1"],
            "arg2": input_data["arg2"],
            "operator": "-",
            "result": input_data["arg1"] - input_data["arg2"]
        }
    )


if __name__ == '__main__':
    app.run()
