from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.json

    latitude = data["latitude"]
    longitude = data["longitude"]

    print("Latitude:", latitude)
    print("Longitude:", longitude)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)