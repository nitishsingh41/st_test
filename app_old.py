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
            # Ask a question
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # React to user input
            if prompt := st.chat_input("What is up?"):
                # Display user message in chat message container
                st.chat_message("user").markdown(prompt)
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
            
                response = f"Echo: {prompt}"
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})

      


    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
