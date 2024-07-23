import streamlit as st
import requests
from io import BytesIO

st.title("PDF/TXT/Website Chat Bot")

# Create a sidebar for source selection and file upload
st.sidebar.header("Upload Source")

# Select source type in the sidebar
source_type = st.sidebar.selectbox("Select Source Type", options=['pdf', 'txt', 'website'])

# Input based on selected source type in the sidebar
if source_type == 'pdf':
    uploaded_pdf = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
    web_url = None  # Ensure web_url is not used if PDF is selected
elif source_type == 'txt':
    uploaded_txt = st.sidebar.file_uploader("Upload a TXT file", type=["txt"])
    web_url = None  # Ensure web_url is not used if TXT is selected
else:  # website
    uploaded_pdf = None  # Ensure file upload is not used if website is selected
    uploaded_txt = None
    web_url = st.sidebar.text_input("Enter Website URL:", value="https://example.com")

# New submit button to upload file and start chat
if st.sidebar.button("Upload and Start Chat"):
    try:
        if source_type == 'pdf':
            if uploaded_pdf is not None:
                with open("uploaded_document.pdf", "wb") as f:
                    f.write(uploaded_pdf.getbuffer())
                st.success("PDF uploaded successfully.")
                source_path = "uploaded_document.pdf"
            else:
