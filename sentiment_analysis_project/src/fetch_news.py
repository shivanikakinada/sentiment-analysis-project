from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(response.text)

    data = response.json()

    rows = []

    for article in data["articles"]:
        rows.append({
            "source": article["source"]["name"],
            "title": article["title"],
            "description": article["description"],
            "published_at": article["publishedAt"]
        })

    return pd.DataFrame(rows)