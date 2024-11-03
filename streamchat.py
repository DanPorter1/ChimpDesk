# streamlit run d:/Py/Work/ai/streamlit/streamchat.py
import os
import streamlit as st 
from fucs import * 

avatar = r"D:\Py\Work\ai\streamlit\chimp.jpg"
avatarsd = r"D:\Py\Work\ai\streamlit\sda.jpg"
# # Display the image
# st.image(r"D:\Py\Work\ai\streamlit\chimp.jpg")
with st.sidebar:
    st.image(r"D:\Py\Work\ai\streamlit\chimp.jpg")
    st.write("I'm here to help you with some tasks")
# # Set the title

st.title("Chimpanze Service Desk")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatarsd"] if message["role"] == "user" else message["avatar"] if message["role"] == "assistant" else None):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your message... "):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, "avatarsd": avatarsd})
    # Display user message in chat message container
    with st.chat_message("user", avatar=avatarsd):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=avatar):
        # Logic for respose
        if any(word in prompt.lower() for word in ["email", "mail"]):
            response = st.write(email(prompt))
        else:
            response = "Sorry I didn't understand that"
            st.write(response)
            #response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response, "avatar": avatar})