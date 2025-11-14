import streamlit as st
import requests

st.title("Social Media Comment Analyzer")

user_input = st.text_area("Enter a comment")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a comment")
    else:
        url = "http://127.0.0.1:8000/predict/"

        payload = {"text": user_input}

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            result = response.json()["prediction"]
            st.success(f"Prediction: {result}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
