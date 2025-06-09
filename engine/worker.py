from flask import Flask, request
from multiprocessing import Process
from scraper import scrape_url

app = Flask(__name__)

@app.route("/scrape", methods=["POST"])
def handle_scrape():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return {"error": "Missing URL"}, 400

    process = Process(target=scrape_url, args=(url,))
    process.start()

    return {"status": "Scraping started"}, 202

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
