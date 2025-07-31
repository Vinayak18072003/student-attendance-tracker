from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    if os.path.exists("../attendance_data.json"):
        with open("../attendance_data.json") as f:
            data = json.load(f)
    else:
        data = {}

    return render_template("dashboard.html", attendance=data)

if __name__ == "__main__":
    app.run(debug=True)
