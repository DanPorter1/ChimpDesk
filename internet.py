def internet_issue():
    """Simulates the troubleshooting flowchart for internet issues."""

    # Initial question
    internet_status = input("Does the customer have internet? (Yes/No): ")

    if internet_status.lower() == "yes":
        print("Other issue. Please escalate.")
    else:
        router_lights = input("Are the lights on the router? (Yes/No): ")

        if router_lights.lower() == "yes":
            cd_light_status = input("Is the CD light on SOLID? (Yes/No): ")
            if cd_light_status.lower() == "yes":
                ping_status = input("Can you ping the 'Default Gateway'? (Yes/No): ")
                if ping_status.lower() == "yes":
                    print("Escalate if there are still issues.")
                else:
                    print("Raise to RC - Do they have a Failover?")
            else:
                dsl_check = input("DSL Check router and OR Socket, Reboot Router, CD Light Solid? (Yes/No): ")
                if dsl_check.lower() == "yes":
                    ping_status = input("Can you ping the 'Default Gateway'? (Yes/No): ")
                    if ping_status.lower() == "yes":
                        print("Escalate if there are still issues.")
                    else:
                        print("Raise to RC - Do they have a Failover?")
                else:
                    print("Raise to RC - Do they have a Failover?")
        else:
            reboot_status = input("Reboot router are the lights now on? (Yes/No): ")
            if reboot_status.lower() == "yes":
                cd_light_status = input("Is the CD light on SOLID? (Yes/No): ")
                if cd_light_status.lower() == "yes":
                    ping_status = input("Can you ping the 'Default Gateway'? (Yes/No): ")
                    if ping_status.lower() == "yes":
                        print("Escalate if there are still issues.")
                    else:
                        print("Raise to RC - Do they have a Failover?")
                else:
                    dsl_check = input("DSL Check router and OR Socket, Reboot Router, CD Light Solid? (Yes/No): ")
                    if dsl_check.lower() == "yes":
                        ping_status = input("Can you ping the 'Default Gateway'? (Yes/No): ")
                        if ping_status.lower() == "yes":
                            print("Escalate if there are still issues.")
                        else:
                            print("Raise to RC - Do they have a Failover?")
                    else:
                        print("Raise to RC - Do they have a Failover?")
            else:
                print("Raise to RC - Do they have a Failover?")

# Call the function to start the troubleshooting process
troubleshoot_internet_issue()
