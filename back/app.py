from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/text", methods=["GET", "POST"])
def text():
    if request.method == "GET":
        return "GETです"
    else:
        post_data = request.args.get("code")
        print("This", post_data)
        return post_data


@app.route("/image", methods=["GET", "POST"])
def image():
    if request.method == "GET":
        return "GETです"
    else:
        post_data = request.args.get("data")
        return post_data


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, threaded=True)
