from Hello import *
from PIL import Image
from prompts import *

st.set_page_config(page_title="Chimp Chat", page_icon="🐵")

if not st.session_state.authentication_status:
    st.info('Please Login from the Home page and try again.')
    st.stop()

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")

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

# Initialize chat history
if "messages" not in st.session_state:
        st.session_state.messages = []

if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "assistant", "content": """
    Hello! 👋 I'm here to help you with ticket logging, troubleshooting internet issues, and answering any questions you may have.

If you're experiencing a problem, let me know, and I’ll guide you through some quick troubleshooting steps. Need to log a support ticket instead? I can help with that too!

Just type in your issue, and let's get started. 😊""", "avatar": avatar})
    
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
