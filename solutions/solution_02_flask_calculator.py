from flask import Flask, request

app = Flask(__name__)


@app.route("/add/<int:arg1>/<int:arg2>")
def add(arg1, arg2):
    return str(arg1 + arg2)


@app.route("/div/<int:arg1>/<int:arg2>")
def div(arg1, arg2):
    try:
        if request.args.get("truediv", "true").lower() == "false":
            return str(arg1 // arg2)
        else:
            return str(arg1 / arg2)
    except ZeroDivisionError:
        return "Division by zero."


if __name__ == '__main__':
    app.run()
