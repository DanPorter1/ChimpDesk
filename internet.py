import streamlit as st

def ask_yes_no(question):
    """Ask a yes/no question and return True for 'Yes' and False for 'No'."""
    answer = st.radio(question, ('Yes', 'No'))
    return answer == 'Yes'

def internet():
    """Run the troubleshooting flow for the router."""
    st.title("Router Troubleshooter")
    
    # Step 1: Check if customer has internet
    has_internet = ask_yes_no("Does the Customer have internet?")
    if has_internet:
        st.write("Issue: Other issue detected.")
        return  # End the function, issue detected elsewhere
    
    # Step 2: Check router lights
    lights_on_router = ask_yes_no("Are the lights on the router?")
    
    # If lights are on
    if lights_on_router:
        cd_light_solid = ask_yes_no("Is the CD light on SOLID?")
        if cd_light_solid:
            # If CD light is solid, check if the gateway can be pinged
            can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
            if can_ping_gateway:
                st.write("Action: Escalate if there are still issues.")
            else:
                # If you can't ping the gateway, perform DSL check
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
            # If CD light isn't solid, reboot router and check again
            reboot_router = ask_yes_no("Reboot router. Are the lights now on?")
            if reboot_router:
                cd_light_solid = ask_yes_no("Is the CD light on SOLID?")
                if cd_light_solid:
                    can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                    if can_ping_gateway:
                        st.write("Action: Escalate if there are still issues.")
                    else:
                        # If you still can't ping the gateway, perform DSL check
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
    else:
        # If lights aren't on, reboot router
        reboot_router = ask_yes_no("Reboot router. Are the lights now on?")
        if reboot_router:
            cd_light_solid = ask_yes_no("Is the CD light on SOLID?")
            if cd_light_solid:
                can_ping_gateway = ask_yes_no("Can you ping the 'Default Gateway'?")
                if can_ping_gateway:
                    st.write("Action: Escalate if there are still issues.")
                else:
                    # Perform DSL check if the CD light is solid but still can't ping
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
