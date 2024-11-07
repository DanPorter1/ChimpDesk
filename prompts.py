import google.generativeai as genai


api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def dan(prompt):
    response = model.generate_content(prompt)
    return response.text

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

def wemail(wemailprompt):
    # signiture = "\n\nDaniel"
    template = """
        You are a helpful assistant that drafts an email.
        
        You goal is help the user quickly create a perfect email written professionally.
        Keep your reply short and to the point containing the nessessary information. 
        """
    # .format(signiture)
    
    message = template + wemailprompt
    response = model.generate_content(message)
    return response.text

def sd(sdprompt):
    template = """
        
        You are a helpful assistant that assists with logging tickets for a service desk.
        I just need a description of the probem/incident as logged from a service desk anaylist after speaking to a customer. 
        Make this as detialed as possible with bullet points so its easier to read. 
        Don't request further information. 
        Check this website for suggestions https://help.cegedim-healthcare.co.uk/Pharmacymanager/Content/Home.htm
        Can you also make 3 quick suggestions on what may be the cause?
        Issue: 
        """
    
    message = template + sdprompt
    response = model.generate_content(message)
    return response.text

def story(storyprompt):
    template = """
        
        You are a helpful assistant that assists with logging tickets for a service desk.
        I just need a description of the probem/incident as logged from a service desk anaylist after speaking to a customer. 
        Make this as detialed as possible with bullet points so its easier to read. 
        Don't request further information. 
        Check this website for suggestions https://help.cegedim-healthcare.co.uk/Pharmacymanager/Content/Home.htm
        Can you make this into a fantasy story with some fictional characters. 
        Add 2 or 3 lines of your choice of fantasy with suggesting a way to resolve the issue. 
        Issue: 
        """
    
    message = template + storyprompt
    response = model.generate_content(message)
    return response.text

def printer(printerprompt):
    template = """
        
        You are a helpful assistant that assists with logging tickets for a service desk.
        I just need a description of the probem/incident as logged from a service desk anaylist after speaking to a customer. 
        Don't request further information. 
        Can you also make 3 quick suggestions on what may be the cause?
        Printers used: (Label printers:Zebra ZD421, Zebra GK420), (A4 printers: Brother HL6400DW)
        Issue: 
        """
    
    message = template + printerprompt
    response = model.generate_content(message)
    return response.text

def hscn(hscnprompt):
    template = """
        
        You are a helpful assistant that assists with troubleshooting internet issues mainly on a LAN connection. 
        Router used is a Cisco ISR 900-4p - This connects to a switch then to multiple devices. 
        DHCP is active and auto configuration is on. 
        Incidents then get raised to Redcentric Provider
        Also suggest checking if site has a 4G backup - Teltonika RUTX 4G. 
        Not able to access Router interface or configuartion is this done via Redcentric. 
        Only give me Possible Causes and Troubleshooting Steps
        """
    
    message = template + hscnprompt
    response = model.generate_content(message)
    return response.text

def howto(howtoprompt):
    template = """
        
        You are a document writer on a how to guide, expalining the techincal terms in a manner anyone can understand. 
        Customers should be able to follow these instructions clearly without needing to ask more questions. 
        This should be presentable and descriptive. 
        """
    
    message = template + howtoprompt
    response = model.generate_content(message)
    return response.text
