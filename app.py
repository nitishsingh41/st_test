import streamlit as st
import requests
from io import BytesIO

st.title("PDF/TXT/Website Chat Bot")

# Select source type
source_type = st.selectbox("Select Source Type", options=['pdf', 'txt', 'website'])

# Input based on selected source type
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
                st.success("PDF uploaded successfully.")
                source_path = "uploaded_document.pdf"
            else:
                st.error("Please upload a PDF file.")
                source_path = None
        elif source_type == 'txt':
            if uploaded_txt is not None:
                with open("uploaded_document.txt", "wb") as f:
                    f.write(uploaded_txt.getbuffer())
                st.success("TXT file uploaded successfully.")
                source_path = "uploaded_document.txt"
            else:
                st.error("Please upload a TXT file.")
                source_path = None
        else:  # website
            if web_url:
                source_path = web_url
                st.success("Website URL accepted.")
            else:
                st.error("Please enter a valid website URL.")
                source_path = None
        
        if source_path is not None:
            # Chat interface
            chat_input = st.chat_input("Type your message here...")

            if chat_input:
                # Here you would typically process the chat_input
                st.chat_message("user", chat_input)  # Display user's message
                # For demonstration, echoing the input as the bot's response
                st.chat_message("bot", f"You said: {chat_input}")  # Display bot's response

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
