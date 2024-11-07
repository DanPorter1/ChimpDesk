from main import st, Image

avatar = Image.open("chimp.jpg")
avatarsd = Image.open("sda.jpg")

def internet(a):
    # Initial question
    prompt = "Does the customer have internet? (Yes/No):"
    st.chat_message("assistant", avatar=avatar, text=prompt)
    internet_status = st.chat_input(placeholder="Enter your response")

    if internet_status.lower() == "yes":
        st.chat_message("user", avatar=avatarsd, text=internet_status)
        st.chat_message("assistant", avatar=avatar, text="Other issue. Please escalate.")
    else:
        # Router lights check
        router_lights = st.chat_input("Are the lights on the router? (Yes/No):")
        if router_lights.lower() == "yes":
            # CD light check
            cd_light_status = st.chat_input("Is the CD light on SOLID? (Yes/No):")
            if cd_light_status.lower() == "yes":
                # Ping check
                ping_status = st.chat_input("Can you ping the 'Default Gateway'? (Yes/No):")
                if ping_status.lower() == "yes":
                    st.chat_message("user", avatar=avatarsd, text=ping_status)
                    st.chat_message("assistant", avatar=avatar, text="Escalate if there are still issues.")
                else:
                    st.chat_message("user", avatar=avatarsd, text=ping_status)
                    st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
            else:
                # DSL check
                dsl_check = st.chat_input("DSL Check router and OR Socket, Reboot Router, CD Light Solid? (Yes/No):")
                if dsl_check.lower() == "yes":
                    ping_status = st.chat_input("Can you ping the 'Default Gateway'? (Yes/No):")
                    if ping_status.lower() == "yes":
                        st.chat_message("user", avatar=avatarsd, text=ping_status)
                        st.chat_message("assistant", avatar=avatar, text="Escalate if there are still issues.")
                    else:
                        st.chat_message("user", avatar=avatarsd, text=ping_status)
                        st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
                else:
                    st.chat_message("user", avatar=avatarsd, text=dsl_check)
                    st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
        else:
            # Reboot router
            reboot_status = st.chat_input("Reboot router are the lights now on? (Yes/No):")
            if reboot_status.lower() == "yes":
                # CD light check
                cd_light_status = st.chat_input("Is the CD light on SOLID? (Yes/No):")
                if cd_light_status.lower() == "yes":
                    # Ping check
                    ping_status = st.chat_input("Can you ping the 'Default Gateway'? (Yes/No):")
                    if ping_status.lower() == "yes":
                        st.chat_message("user", avatar=avatarsd, text=ping_status)
                        st.chat_message("assistant", avatar=avatar, text="Escalate if there are still issues.")
                    else:
                        st.chat_message("user", avatar=avatarsd, text=ping_status)
                        st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
                else:
                    # DSL check
                    dsl_check = st.chat_input("DSL Check router and OR Socket, Reboot Router, CD Light Solid? (Yes/No):")
                    if dsl_check.lower() == "yes":
                        ping_status = st.chat_input("Can you ping the 'Default Gateway'? (Yes/No):")
                        if ping_status.lower() == "yes":
                            st.chat_message("user", avatar=avatarsd, text=ping_status)
                            st.chat_message("assistant", avatar=avatar, text="Escalate if there are still issues.")
                        else:
                            st.chat_message("user", avatar=avatarsd, text=ping_status)
                            st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
                    else:
                        st.chat_message("user", avatar=avatarsd, text=dsl_check)
                        st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
            else:
                st.chat_message("user", avatar=avatarsd, text=reboot_status)
                st.chat_message("assistant", avatar=avatar, text="Raise to RC - Do they have a Failover?")
