from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World. This is version2"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
