import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./uploads"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["JSON_AS_ASCII"] = False
CORS(app, origins=["http://localhost:3000/"])


@app.route("/text", methods=["GET", "POST"])
def text():
    if request.method == "GET":
        return "GETです"
    else:
        post_data = request.args.get("code")
        return post_data


@app.route("/image", methods=["GET", "POST"])
def image():
    if request.method == "GET":
        return "GETです"
    else:
        print("フォーム", request.form)
        fileStorageObj = request.files["img"]
        filename = secure_filename(fileStorageObj.filename)
        fileStorageObj.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"message": "アップロード成功"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, threaded=True)
