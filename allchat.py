# streamlit run d:/Py/Work/ai/streamlit/streamchat.py
import os
import streamlit as st 
import random 
import time
import os
import google.generativeai as genai

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure()
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")
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
    signiture = "\n\nDaniel"
    template = """
        
        You are a helpful assistant that drafts an email reply based on an a new email.
        
        You goal is help the user quickly create a perfect email reply by.
        
        Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
        
        Make sure to sign of with {}.
        
        """.format(signiture)
    
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
