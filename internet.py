from main import st, Image

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")

def internet(a):
    # Initial question
    prompt = "Does the customer have internet? (Yes/No):"
    
    with st.chat_message("assistant", avatar=avatar):
        st.write(prompt)
    
    internet_status = st.chat_input("Enter your message... ")
    
    if internet_status.lower() == "yes":
        with st.chat_message("user", avatar=avatarsd):
            st.markdown(internet_status)
    
    # Move this outside the previous chat message block
    with st.chat_message("assistant", avatar=avatar):
        st.write("Other issue. Please escalate.")
