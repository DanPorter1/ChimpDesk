import streamlit as st 
import os
from PIL import Image
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(page_title="Service Desk", page_icon="💻")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

st.title("""Welcome to Your AI-Powered Support Assistant""")
st.write("""
Effortlessly manage and resolve your technical issues with our AI-driven support assistant. Whether you’re experiencing internet problems or need help with basic troubleshooting, this app is designed to make support simpler and faster.

Features
Chat with AI for Assistance: Our intelligent chat assistant is here to guide you through common issues, answer your questions, and provide real-time troubleshooting for internet and connectivity problems.

Log Support Tickets: Easily log support tickets with our intuitive interface. Just follow the prompts, and your issue will be documented and ready for follow-up.

Automated Troubleshooting: Get instant help with common internet issues. Our AI will walk you through basic troubleshooting steps to save time and help you get back online.

How to Use the App
Simply start by interacting with the chat assistant, and it will assist you in diagnosing and resolving issues. If needed, you can log a support ticket directly through the app, making it easy to get the help you need.

Let’s get started and make support easy, accessible, and efficient!""")

authenticator.login('sidebar')
# # Set the title
# authenticator.login()
if st.session_state['authentication_status']:
    with st.sidebar:
        st.title(f'Welcome *{st.session_state["name"]}*')
        st.session_state.messages = []
        authenticator.logout()
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
