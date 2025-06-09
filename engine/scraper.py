import requests
from bs4 import BeautifulSoup
import re
from db import save_result
from datetime import datetime
from zoneinfo import ZoneInfo

def scrape_url(url):
    print(f"[Engine] Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[Engine] Error: status {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "Brak tytułu"
        headers = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
        links = [a['href'] for a in soup.find_all('a', href=True)]
        emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)))

        result = {
            "url": url,
            "title": title,
            "headers": headers,
            "links": links,
            "emails": emails,
            "timestamp": datetime.now(ZoneInfo("Europe/Warsaw"))
        }

        save_result(result)
        print(f"[Engine] Saved result for: {url}")

    except Exception as e:
        print(f"[Engine] Error scraping {url}: {e}")
