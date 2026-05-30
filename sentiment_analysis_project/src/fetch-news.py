from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()


API_KEY = os.getenv("NEWS_API_KEY")

url = (
    f"https://newsapi.org/v2/everything?"
    f"q=artificial intelligence&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

print(response.status_code)
data = response.json()
print (data.keys()) #printing only keys in the response :output is status,totalresults,articles

articles= data["articles"]
rows = [] # initialising with empty rows

for article in articles: #appending required columns
        rows.append({
        "title": article["title"],
        "description": article["description"],
        "published_at": article["publishedAt"]
    })
        
df = pd.DataFrame(rows)

df.to_csv(                    #converting dataframe to csv and storing in a folder
    "data/news.csv",
    index=False
)

print("Saved Successfully")
