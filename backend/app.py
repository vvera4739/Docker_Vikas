from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask backend is running successfully!"
    })


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    return jsonify({
        "message": "Form submitted successfully!",
        "name": name,
        "email": email
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)