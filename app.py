import streamlit as st
import requests
from io import BytesIO

st.title("PDF/TXT/Website Chat Bot")

source_type = st.selectbox("Select Source Type", options=['pdf', 'txt', 'website'])

if source_type == 'pdf':
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
elif source_type == 'txt':
    uploaded_txt = st.file_uploader("Upload a TXT file", type=["txt"])
else:
    web_url = st.text_input("Enter Website URL:", value="https://example.com")

if st.button("Submit"):
    try:
        if source_type == 'pdf':
            if uploaded_pdf is not None:
                with open("uploaded_document.pdf", "wb") as f:
                    f.write(uploaded_pdf.getbuffer())
                st.write("PDF uploaded successfully.")
                source_path = "uploaded_document.pdf"
            else:
                st.write("Please upload a PDF file.")
                source_path = None
        elif source_type == 'txt':
            if uploaded_txt is not None:
                with open("uploaded_document.txt", "wb") as f:
                    f.write(uploaded_txt.getbuffer())
                st.write("TXT file uploaded successfully.")
                source_path = "uploaded_document.txt"
            else:
                st.write("Please upload a TXT file.")
                source_path = None
        else:  # website
            if web_url:
                source_path = web_url
                st.write("Website URL accepted.")
            else:
                st.write("Please enter a valid website URL.")
                source_path = None
        
        if source_path is not None:
            chat_input = st.text_area("Chat Input", height=200)
            
            if st.button("Send"):
                # Here you would typically process the chat_input
                st.write("Answer:", chat_input)
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")
