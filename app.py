from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

latest_location = {
    "latitude": None,
    "longitude": None,
    "updated_at": None,
    "sharing": False
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/location", methods=["POST"])
def location():
    data = request.get_json(silent=True) or {}

    if data.get("sharing") is False:
        latest_location["sharing"] = False
        return jsonify({"success": True})

    lat = data.get("latitude")
    lon = data.get("longitude")

    if lat is None or lon is None:
        return jsonify({"error": "Coordinates required"}), 400

    latest_location.update({
        "latitude": lat,
        "longitude": lon,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "sharing": True
    })

    return jsonify({"success": True})


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/get-location")
def get_location():
    return jsonify(latest_location)


if __name__ == "__main__":
    app.run(debug=True)
