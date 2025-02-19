from flask import Flask, request, send_file
import os

app = Flask(__name__)


def genImg(t):
    i = {"dog": "dog.jpg", "cat": "cat.jpg", "bird": "bird.jpg"}
    return i.get(t, "default.jpg")


@app.route("/generate", methods=["GET"])
def gen():
    t = request.args.get("type", "dog")
    p = genImg(t)
    return send_file(p, mimetype="image/jpeg")


if __name__ == "__main__":
    p = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=p)
