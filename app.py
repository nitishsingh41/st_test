import streamlit as st
import requests
from io import BytesIO

st.title("PDF/Website Chat Bot")

source_type = st.selectbox("Select Source Type", options=['pdf', 'website'])

if source_type == 'pdf':
    pdf_url = st.text_input("Enter PDF URL:", value="https://example.com/document.pdf")
else:
    web_url = st.text_input("Enter Website URL:", value="https://example.com")

if st.button("Submit"):
    try:
        if source_type == 'pdf':
            response = requests.get(pdf_url)
            response.raise_for_status()  # Raise an error for bad responses
            pdf_bytes = BytesIO(response.content)
            
            with open("document.pdf", "wb") as f:
                f.write(pdf_bytes.getvalue())
            
            st.write("PDF downloaded successfully.")
            source_path = "document.pdf"
        else:
            source_path = web_url
        
        chat_input = st.text_area("Chat Input", height=200)
        
        if st.button("Send"):
            # Here you would typically process the chat_input
            st.write("Answer:", chat_input)
    except requests.exceptions.RequestException as e:
        st.write(f"Error downloading file: {e}")
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")
