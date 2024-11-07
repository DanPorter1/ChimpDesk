import streamlit as st

st.set_page_config(page_title="Internet Checking", page_icon="🌐")

if not st.session_state.authentication_status:
    st.info('Please Login from the Home page and try again.')
    st.stop()

# Define the questions and flow as a dictionary structure for easy navigation
questions = {
    "1": {"text": "Does the Customer have internet?", "yes": "2", "no": "3"},
    "2": {"text": "Other issue.", "end": True},
    "3": {"text": "Are the lights on the router?", "yes": "4", "no": "5"},
    "4": {"text": "Is the CD light on SOLID?", "yes": "7", "no": "8"},
    "5": {"text": "Reboot router. Are the lights now on?", "yes": "4", "no": "6"},
    "6": {"text": "Raise to RC - Chaeck 4G", "end": True},
    "7": {"text": "Can you ping the 'Default Gateway'?", "yes": "9", "no": "9"},
    "8": {"text": "DSL Check router and OR Socket, Reboot Router, CD Light Solid?", "yes": "7", "no": "6"},
    "9": {"text": "Escalate if there are still issues.", "end": True}
}

# Initialize session state for current question, history, and reset flag
if 'current_question' not in st.session_state:
    st.session_state.current_question = "1"  # Start with the first question
if 'history' not in st.session_state:
    st.session_state.history = []

# Title for the app
st.title("Network Diagnostic Tool")

# Display current question and record user's answer
question_id = st.session_state.current_question
question_data = questions[question_id]
st.subheader(question_data["text"])

# Only show answer options if the question is not an end node
if not question_data.get("end"):
    user_input = st.radio("Please select an option:", ("Yes", "No"), key=question_id)

    # Submit button to record answer
    if st.button("Submit Answer"):
        # Save question and answer to history
        st.session_state.history.append((question_data["text"], user_input))
        
        # Move to the next question based on the user's answer
        st.session_state.current_question = question_data[user_input.lower()]
        
        # Rerun to immediately go to the next question
        st.rerun()
else:
    st.info("Troubleshooting concluded. Please use the Reset button to start again.")

# Display the answer history
st.subheader("History of Responses")
if st.session_state.history:
    for idx, (q, a) in enumerate(st.session_state.history, 1):
        st.write(f"{idx}. Question: {q} - Answer: {a}")
else:
    st.write("No responses recorded yet.")

# Reset button to clear history and start over
if st.button("Reset"):
    st.session_state.current_question = "1"
    st.session_state.history = []
    st.info("History has been reset. Starting from the beginning.")
    st.rerun()
