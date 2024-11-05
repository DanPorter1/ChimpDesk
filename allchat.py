# streamlit run d:/Py/Work/ai/streamlit/streamchat.py
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

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(page_title="Chimp Service Desk")
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure()
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")
# # Display the image
# st.image(r"D:\Py\Work\ai\streamlit\chimp.jpg")
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def email(emailprompt):
    # signiture = "\n\nDaniel"
    template = """
        
        You are a helpful assistant that drafts an email reply based on an a new email.
        
        You goal is help the user quickly create a perfect email reply by.
        
        Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
        
        """
    # .format(signiture)
    
    message = template + emailprompt
    response = model.generate_content(message)
    return response.text

def wemail(emailprompt):
    # signiture = "\n\nDaniel"
    template = """
        You are a helpful assistant that drafts an email.
        
        You goal is help the user quickly create a perfect email written professionally.
        Keep your reply short and to the point containing the nessessary information. 
        """
    # .format(signiture)
    
    message = template + emailprompt
    response = model.generate_content(message)
    return response.text

def sd(sdprompt):
    template = """
        
        You are a helpful assistant that assists with logging tickets for a service desk.
        I just need a description of the probem/incident as logged from a service desk anaylist after speaking to a customer. 
        Support desk is for Pharmacies processing prescriptions. 
        Don't request further information. 
        Check this website for suggestions https://help.cegedim-healthcare.co.uk/Pharmacymanager/Content/Home.htm
        Can you also make 3 quick suggestions on what may be the cause?
        Issue: 
        """
    
    message = template + sdprompt
    response = model.generate_content(message)
    return response.text

def printer(sdprompt):
    template = """
        
        You are a helpful assistant that assists with logging tickets for a service desk.
        I just need a description of the probem/incident as logged from a service desk anaylist after speaking to a customer. 
        Don't request further information. 
        Can you also make 3 quick suggestions on what may be the cause?
        Printers used: (Label printers:Zebra ZD421, Zebra GK420), (A4 printers: Brother HL6400DW)
        Issue: 
        """
    
    message = template + sdprompt
    response = model.generate_content(message)
    return response.text

def hscn(sdprompt):
    template = """
        
        You are a helpful assistant that assists with troubleshooting internet issues mainly on a LAN connection. 
        Router used is a Cisco ISR 900-4p - This connects to a switch then to multiple devices. 
        DHCP is active and auto configuration is on. 
        Incidents then get raised to Redcentric Provider
        Also suggest checking if site has a 4G backup - Teltonika RUTX 4G. 
        Not able to access Router interface or configuartion is this done via Redcentric. 
        Only give me Possible Causes and Troubleshooting Steps
        """
    
    message = template + sdprompt
    response = model.generate_content(message)
    return response.text

def howto(sdprompt):
    template = """
        
        You are a document writer on a how to guide, expalining the techincal terms in a manner anyone can understand. 
        Customers should be able to follow these instructions clearly without needing to ask more questions. 
        This should be presentable and descriptive. 
        """
    
    message = template + sdprompt
    response = model.generate_content(message)
    return response.text

# # Set the title
authenticator.login()
if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')

    
    st.title("Chimpanzee Service Desk")

    with st.sidebar:
        st.image("chimp.jpg")
        st.write("I'm here to help you with some tasks")
        st.write("====================")
        st.markdown("""
          Functions - Start your message with these keywords:
          - Email: Responds to email
          - SD: Service Desk Ticket
          - HSCN: Internet issues
          - Printer: Printer-related Issues
        """)
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
                "howto": howto
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
