import streamlit as st
import requests
import pandas as pd
import numpy as np

# Apply Dark Mode Styling
st.set_page_config(page_title="Streamlit App with Dark Mode", page_icon="🌙", layout="wide")
dark_mode = st.toggle("🌙 Enable Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        body { background-color: #222; color: white; }
        .stApp { background-color: #222; color: white; }
        .stButton>button { background-color: #444; color: white; border-radius: 5px; }
        </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Explore the features")

# API Request to FastAPI Backend
st.sidebar.subheader("Fetch Data from API")
if st.sidebar.button("Get Data"):
    response = requests.get("http://127.0.0.1:8000/data")
    if response.status_code == 200:
        st.sidebar.success(f"Received: {response.json()['data']}")
    else:
        st.sidebar.error("Failed to fetch data.")

# Main Content
st.title("🚀 The Best Way to Build Python Apps?")
st.write("This app demonstrates *FastAPI Backend + Streamlit Frontend + Dark Mode*")

# User Input
user_input = st.text_input("Enter something:")
if user_input:
    st.success(f"You entered: {user_input}")

# Charts Example
st.subheader("Random Data Chart")
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=["A", "B", "C"])
st.line_chart(df)

# Button Example
if st.button("Click Me!"):
    st.balloons()