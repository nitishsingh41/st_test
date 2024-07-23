import streamlit as st
import requests
from io import BytesIO

st.title("PDF/TXT/Website Chat Bot")

# Select source type in the sidebar
st.sidebar.header("Select Source Type")
source_type = st.sidebar.selectbox("Choose Source Type", options=['pdf', 'txt', 'website'])

# Input based on selected source type in the sidebar
source_path = None
if source_type == 'pdf':
    uploaded_pdf = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_pdf is not None:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(uploaded_pdf.getbuffer())
        st.sidebar.success("PDF uploaded successfully.")
        source_path = "uploaded_document.pdf"
    else:
        st.sidebar.warning("Please upload a PDF file.")
elif source_type == 'txt':
    uploaded_txt = st.sidebar.file_uploader("Upload a TXT file", type=["txt"])
    if uploaded_txt is not None:
        with open("uploaded_document.txt", "wb") as f:
            f.write(uploaded_txt.getbuffer())
        st.sidebar.success("TXT file uploaded successfully.")
        source_path = "uploaded_document.txt"
    else:
        st.sidebar.warning("Please upload a TXT file.")
else:  # website
    web_url = st.sidebar.text_input("Enter Website URL:", value="https://example.com")
    if web_url:
        source_path = web_url
        st.sidebar.success("Website URL accepted.")
    else:
        st.sidebar.warning("Please enter a valid website URL.")

# Chat functionality
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

    # Here you would typically process the input based on the source
    response = f"Echo: {prompt}"  # Placeholder response
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Handle unexpected errors
try:
    # Your existing code logic goes here
    pass
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
