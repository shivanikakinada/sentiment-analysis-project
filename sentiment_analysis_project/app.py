from dotenv import load_dotenv
import os
import requests
import pandas as pd
import streamlit as st

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

st.title("News Search App")

topic = st.text_input(
    "Enter a topic",
    placeholder="e.g. Artificial Intelligence, Python, AWS"
)

if st.button("Fetch News"):

    if not topic:
        st.warning("Please enter a topic.")
    else:

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={topic}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"apiKey={API_KEY}"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            rows = []

            for article in data["articles"]:
                rows.append({
                    "Source": article["source"]["name"],
                    "Title": article["title"],
                    "Published": article["publishedAt"],
                    "URL": article["url"]
                })

            df = pd.DataFrame(rows)

            st.success(f"Found {len(df)} articles!")

            st.dataframe(df)

            csv = df.to_csv(index=False)

            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{topic}_news.csv",
                mime="text/csv"
            )

        else:
            st.error(f"Failed to fetch news. Status Code: {response.status_code}")
            st.write(response.text)