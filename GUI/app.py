from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from db import get_all_results

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            requests.post("http://engine:5001/scrape", json={"url": url})
        return redirect(url_for("index"))

    results = get_all_results()
    return render_template("index.html", results=results)

@app.route("/api/results", methods=["GET"])
def api_results():
    results = get_all_results()
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)