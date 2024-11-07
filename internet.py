import streamlit as st

def internet(prompt):
    # Initialize session state variables if they don't exist
    if "internet_step" not in st.session_state:
        st.session_state.internet_step = 0  # Track which step of the conversation we are in
        st.session_state.internet_responses = []  # Store responses

    # Define the steps of the conversation
    steps = [
        {
            "question": "Does the customer have internet? (Yes/No):",
            "next_step": 1
        },
        {
            "question": "Are the lights on the router? (Yes/No):",
            "next_step": 2
        },
        {
            "question": "Is the CD light on SOLID? (Yes/No):",
            "next_step": 3
        },
        {
            "question": "Can you ping the 'Default Gateway'? (Yes/No):",
            "next_step": 4
        },
        {
            "question": "Reboot the router and check again. Are the lights on now? (Yes/No):",
            "next_step": 5
        },
        {
            "question": "DSL Check router and OR Socket, Reboot Router, CD Light Solid? (Yes/No):",
            "next_step": 6
        }
    ]

    # Determine the current step based on session state
    current_step = st.session_state.internet_step

    if current_step == 0:
        # First question (Does the customer have internet?)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        internet_status = st.chat_input("Enter your message... ")
        
        if internet_status.lower() == "yes":
            st.session_state.internet_responses.append(internet_status)
            st.session_state.internet_step = 1  # Proceed to the next step
            return "Other issue. Please escalate."
        else:
            st.session_state.internet_responses.append(internet_status)
            st.session_state.internet_step = 1
            return "Let's check the router lights."

    elif current_step == 1:
        # Second question (Are the lights on the router?)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        router_lights = st.chat_input("Enter your message... ")
        
        if router_lights.lower() == "yes":
            st.session_state.internet_responses.append(router_lights)
            st.session_state.internet_step = 2  # Move to the next step
            return "Great! Let's check if the CD light is on SOLID."
        else:
            st.session_state.internet_responses.append(router_lights)
            st.session_state.internet_step = 1
            return "Try rebooting the router and check the lights again."

    elif current_step == 2:
        # Third question (Is the CD light on SOLID?)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        cd_light_status = st.chat_input("Enter your message... ")

        if cd_light_status.lower() == "yes":
            st.session_state.internet_responses.append(cd_light_status)
            st.session_state.internet_step = 3  # Move to the next step
            return "Can you ping the 'Default Gateway'?"
        else:
            st.session_state.internet_responses.append(cd_light_status)
            st.session_state.internet_step = 2
            return "Check your DSL connection, router, and OR socket. Reboot if needed."

    elif current_step == 3:
        # Fourth question (Can you ping the 'Default Gateway'?)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        ping_status = st.chat_input("Enter your message... ")

        if ping_status.lower() == "yes":
            st.session_state.internet_responses.append(ping_status)
            st.session_state.internet_step = 4  # Proceed to the next step
            return "Escalate if there are still issues."
        else:
            st.session_state.internet_responses.append(ping_status)
            st.session_state.internet_step = 3
            return "Let's raise this to RC. Do you have a failover?"

    elif current_step == 4:
        # Fifth question (Reboot router and check again)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        reboot_status = st.chat_input("Enter your message... ")

        if reboot_status.lower() == "yes":
            st.session_state.internet_responses.append(reboot_status)
            st.session_state.internet_step = 5  # Move to the next step
            return "Great! Let's check the DSL connection."
        else:
            st.session_state.internet_responses.append(reboot_status)
            st.session_state.internet_step = 4
            return "Please reboot the router and check again."

    elif current_step == 5:
        # Sixth question (DSL check)
        st.chat_message("assistant", avatar="chimp.jpg").markdown(steps[current_step]["question"])
        dsl_check = st.chat_input("Enter your message... ")

        if dsl_check.lower() == "yes":
            st.session_state.internet_responses.append(dsl_check)
            st.session_state.internet_step = 6  # Final step
            return "Escalate if issues persist."
        else:
            st.session_state.internet_responses.append(dsl_check)
            st.session_state.internet_step = 5
            return "Please check your DSL connection, reboot the router, and check the CD light again."

    elif current_step == 6:
        # End of the flow
        st.session_state.internet_step = 0  # Reset the step for next interaction
        return "Thank you! You've completed the troubleshooting steps."

    else:
        return "Sorry, something went wrong. Please try again."
