import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="AI-Based Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# 2. Read your HTML file
with open("Smart_Irrigation_Updated.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 3. Render the HTML content
# We use a large height to ensure your full report is visible
components.html(html_data, height=2500, scrolling=True)
