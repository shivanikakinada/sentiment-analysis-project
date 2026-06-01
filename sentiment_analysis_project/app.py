import streamlit as st
from src.fetch_news import fetch_news
from src.sentiment import analyze_sentiment
from src.visualize import sentiment_chart

st.title("News Sentiment Analyzer")

topic = st.text_input("Enter a topic")

if st.button("Fetch News"):

    df = fetch_news(topic)
    df = analyze_sentiment(df)

    st.dataframe(df)
    fig = sentiment_chart(df)
    st.pyplot(fig)