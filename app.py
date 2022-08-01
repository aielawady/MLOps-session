from flask import Flask, request
from main import add

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/version")
def version():
    return "0.0.1"

@app.route("/predict", methods=["POST"])
def predict():
    values = request.json
    x = values["x"]
    y = values["y"]
    result = add(x, y)
    return {"result": result}

@app.route("/predict_get/<int:x>/<int:y>", methods=["GET"])
def predict_get(x, y):
    result = add(x, y)
    return str(result)

@app.route("/asd")
def asd():
    sub(2,6)
    return 

if __name__ == "__main__":
    app.run()