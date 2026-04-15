import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI-Based Smart Irrigation",
    page_icon="🌱",
    layout="wide"
)

# 2. Tabs for Organization
# This lets you switch between your Report and your Presentation
tab1, tab2 = st.tabs(["📄 Project Report", "📊 Presentation"])

with tab1:
    # Use the HTML file we already set up
    st.iframe("Smart_Irrigation_Updated.html", height=2000)

with tab2:
    st.subheader("Project Review III Presentation")
    # If you converted your PPT to PDF (recommended for stability)
    st.iframe("Your_Presentation_File.pdf", height=800)
    
    # Or add a download button for the raw PPTX
    with open("Smart_Irrigation_Presentation.pptx", "rb") as file:
        st.download_button(
            label="📥 Download PowerPoint (PPTX)",
            data=file,
            file_name="Smart_Irrigation_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
