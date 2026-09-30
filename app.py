from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

latest_location = {
    "latitude": None,
    "longitude": None
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/location", methods=["POST"])
def location():
    data = request.json

    latest_location["latitude"] = data["latitude"]
    latest_location["longitude"] = data["longitude"]

    print("Latitude:", data["latitude"])
    print("Longitude:", data["longitude"])

    return jsonify({"success": True})


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/get-location")
def get_location():
    return jsonify(latest_location)


if __name__ == "__main__":
    app.run(debug=True)
