import streamlit as st

def ask_yes_no(question):
    """Ask a yes/no question and return True for 'Yes' and False for 'No'."""
    answer = st.radio(question, ('Yes', 'No'))
    return answer == 'Yes'

def internet():
    """Function to run the flowchart logic for router troubleshooting."""
    st.title("Router Troubleshooter")

    has_internet = ask_yes_no("Does the Customer have internet?")
    
    if has_internet:
        st.write("Issue: Other issue detected.")
        return  # End here if the internet is working but there's another issue.
    
    # If no internet, proceed with troubleshooting the router
    lights_on_router = ask_yes_no("Are the lights on the router?")
    
    if lights_on_router:
        cd_light_solid = ask_yes_no("Is the CD light on SOLID?")
        if cd_light_solid:
            can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
            if can_ping_gateway:
                st.write("Action: Escalate if there are still issues.")
            else:
                # Perform DSL check
                dsl_check = ask_yes_no("DSL Check router and OR Socket, Reboot Router, CD Light Solid?")
                if dsl_check:
                    can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                    if can_ping_gateway:
                        st.write("Action: Escalate if there are still issues.")
                    else:
                        st.write("Action: Raise to RC - Do they have a Failover?")
                else:
                    st.write("Action: Raise to RC - Do they have a Failover?")
        else:
            # Reboot router and check lights
            reboot_router = ask_yes_no("Reboot router. Are the lights now on?")
            if reboot_router:
                can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                if can_ping_gateway:
                    st.write("Action: Escalate if there are still issues.")
                else:
                    # Perform DSL check
                    dsl_check = ask_yes_no("DSL Check router and OR Socket, Reboot Router, CD Light Solid?")
                    if dsl_check:
                        can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                        if can_ping_gateway:
                            st.write("Action: Escalate if there are still issues.")
                        else:
                            st.write("Action: Raise to RC - Do they have a Failover?")
                    else:
                        st.write("Action: Raise to RC - Do they have a Failover?")
    else:
        # If lights aren't on, ask for reboot
        reboot_router = ask_yes_no("Reboot router. Are the lights now on?")
        if reboot_router:
            cd_light_solid = ask_yes_no("Is the CD light on SOLID?")
            if cd_light_solid:
                can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                if can_ping_gateway:
                    st.write("Action: Escalate if there are still issues.")
                else:
                    # Perform DSL check
                    dsl_check = ask_yes_no("DSL Check router and OR Socket, Reboot Router, CD Light Solid?")
                    if dsl_check:
                        can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                        if can_ping_gateway:
                            st.write("Action: Escalate if there are still issues.")
                        else:
                            st.write("Action: Raise to RC - Do they have a Failover?")
                    else:
                        st.write("Action: Raise to RC - Do they have a Failover?")
        else:
            st.write("Action: Raise to RC - Do they have a Failover?")
