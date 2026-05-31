from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

# Available topics
topics = {
    1: "artificial intelligence",
    2: "python",
    3: "aws",
    4: "docker",
    5: "kubernetes",
    6: "cybersecurity",
    7: "machine learning",
    8: "data science"
}

print("\nAvailable Topics:")
for num, topic in topics.items():
    print(f"{num}. {topic}")

choice = int(input("\nSelect a topic number: "))

if choice not in topics:
    print("Invalid choice!")
    exit()

selected_topic = topics[choice]

print(f"\nFetching news for: {selected_topic}")

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={selected_topic}&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch news")
    print(response.text)
    exit()

data = response.json()

rows = []

for article in data["articles"]:
    rows.append({
        "source": article["source"]["name"],
        "title": article["title"],
        "description": article["description"],
        "published_at": article["publishedAt"]
    })

df = pd.DataFrame(rows)

filename = selected_topic.replace(" ", "_") + "_news.csv"

df.to_csv(
    f"data/{filename}",
    index=False
)

print(f"\nSaved {len(df)} articles to data/{filename}")