import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI-Based Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# 2. Path to your HTML file
# Streamlit Cloud var file path direct vaparta yeto
html_file_path = "Smart_Irrigation_Updated.html"

# 3. Use st.logo or title if needed
st.title("Smart Irrigation Project Report")

# 4. Use st.iframe (Streamlit's new standard for 2026)
# Height tumchya report nusar adjust kara
st.iframe(html_file_path, height=2500, scrolling=True)
