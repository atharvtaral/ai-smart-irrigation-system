import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI-Based Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# 2. Path to your HTML file
html_file_path = "Smart_Irrigation_Updated.html"

# 3. Use st.iframe (Standard for 2026)
# Simply remove the 'scrolling' argument to fix the TypeError
st.iframe(html_file_path, height=2500)
