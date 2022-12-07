import streamlit as st
from PIL import Image

st.write("""
         # Welcome
         Welcome to our final project for **Introduction to AI Development**.
         We want show you some interested data about Crypto currency
         Team member:
         - Shenglin Qian
         - Nandor
         - Bavithra
         """)
image1 = Image.open("top_10_percent.jpg")
st.image(image1,caption="Top 10 Crypto Currency's Market Cap to Total Market")

image2 = Image.open("top10_daily_change.jpg")
st.image(image2,caption="Top 10 Crypto Currency's Daily Change")

image3 = Image.open("top10_details.jpg")
st.image(image3,caption="Top 10 Crypto Currency's Market Share")