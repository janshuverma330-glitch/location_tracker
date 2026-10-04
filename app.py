
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
def receive_location():
    data = request.get_json(silent=True) or {}

    # Stop sharing when the user presses Stop
    if data.get("sharing") is False:
        latest_location["sharing"] = False
        return jsonify({"success": True})

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if latitude is None or longitude is None:
        return jsonify({"error": "Coordinates are required"}), 400

    try:
        latitude = float(latitude)
        longitude = float(longitude)

        if not (-90 <= latitude <= 90):
            raise ValueError()

        if not (-180 <= longitude <= 180):
            raise ValueError()

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid coordinates"}), 400

    latest_location.update({
        "latitude": latitude,
        "longitude": longitude,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "sharing": True
    })

    print("Location update received:", latest_location)

    return jsonify({"success": True})


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/get-location")
def get_location():
    return jsonify(latest_location)


if __name__ == "__main__":
    app.run(debug=True)
