import os
import streamlit as st 
import random 
import time
import os
import google.generativeai as genai
from PIL import Image
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from prompts import *

st.set_page_config(page_title="Chimp Service Desk")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
##
## TEMP - GEMINI_API_KEY="AIzaSyCB-4dPxlgELGpK22eaKfTwBf1OTQFjbuA"
##
api_key="AIzaSyCB-4dPxlgELGpK22eaKfTwBf1OTQFjbuA"
#api_key = st.secrets["GEMINI_API_KEY"]
genai.configure()
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")
# # Display the image
# st.image(r"D:\Py\Work\ai\streamlit\chimp.jpg")


# # Set the title
authenticator.login()
if st.session_state['authentication_status']:
    st.write(f'Welcome *{st.session_state["name"]}*')

    
    st.title("Chimpanzee Service Desk")

    with st.sidebar:
        st.image("chimp.jpg")
        st.write("I'm here to help you with some tasks")
        st.write("====================")
        st.markdown("""
          Functions - Start your message with these keywords:
          - SD: Service Desk Ticket
          - Email: Responds to email
          - Wemail: Writes email
          - HSCN: Internet issues
          - Printer: Printer-related Issues
          - Howto: Writes how-to document
        """)
        authenticator.logout()
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
            keyword_functions = {
                "email": email,
                "wemail": wemail,
                "sd": sd,
                "hscn": hscn,
                "printer": printer,
                "howto": howto,
                "story": story,
                "dan": dan,
            }
            
            # Logic for response
            response = "Sorry I didn't understand that"
            for keyword, func in keyword_functions.items():
                if prompt.lower().startswith(keyword):
                    response = func(prompt)
                    break
    
        st.write(response)
                #response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response, "avatar": avatar})
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
