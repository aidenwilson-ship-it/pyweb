from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin from HTML page

messages = []

@app.route("/messages", methods=["GET", "POST"])
def handle_messages():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "").strip()
        text = data.get("text", "").strip()
        if name and text:
            messages.append({"name": name, "text": text})
        return "", 204
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
