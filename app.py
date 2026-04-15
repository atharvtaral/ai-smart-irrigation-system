import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI-Based Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# 2. Function to safely load the HTML
def load_html(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

# 3. Path to your project file
html_content = load_html("Smart_Irrigation_Updated.html")

if html_content:
    # Use st.components.v1.html as a fallback if st.iframe has path issues
    # but wrap it in a container for better display
    st.components.v1.html(html_content, height=2500, scrolling=True)
else:
    st.error("Error: 'Smart_Irrigation_Updated.html' not found in the repository.")
    st.info("Please ensure the filename matches exactly (including uppercase/lowercase).")
