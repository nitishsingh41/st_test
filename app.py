import streamlit as st
import requests
from io import BytesIO

st.title("PDF/Website Chat Bot")

source_type = st.selectbox("Select Source Type", options=['pdf', 'website', 'file'])

if source_type == 'pdf':
    pdf_url = st.text_input("Enter PDF URL:", value="https://example.com/document.pdf")
elif source_type == 'website':
    web_url = st.text_input("Enter Website URL:", value="https://example.com")
else:
    uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])

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
        elif source_type == 'website':
            source_path = web_url
        else:
            if uploaded_file is not None:
                if uploaded_file.name.endswith(".pdf"):
                    with open("document.pdf", "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.write("PDF uploaded successfully.")
                    source_path = "document.pdf"
                elif uploaded_file.name.endswith(".txt"):
                    with open("document.txt", "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.write("TXT file uploaded successfully.")
                    source_path = "document.txt"
                else:
                    st.write("Please upload a PDF or TXT file.")
                    source_path = None
            else:
                st.write("No file uploaded.")
                source_path = None
        
        if source_path is not None:
            chat_input = st.text_area("Chat Input", height=200)
            
            if st.button("Send"):
                # Here you would typically process the chat_input
                st.write("Answer:", chat_input)
    except requests.exceptions.RequestException as e:
        st.write(f"Error downloading file: {e}")
    except Exception as e:
        st.write(f"An unexpected error occurred: {e}")
