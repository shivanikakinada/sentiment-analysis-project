import streamlit as st
import socket
from src.fetch_news import fetch_news

st.title("News Search App")
st.write("Hostname:", socket.gethostname())

topic = st.text_input("Enter a topic")

if st.button("Fetch News"):

    df = fetch_news(topic)

    st.dataframe(df)