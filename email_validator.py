# Get user input for the email ID
email = input("Enter your emailid: ")

# List of valid email domains
email_domains = [
    "gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com", 
    "aol.com", "zoho.com", "protonmail.com", "yandex.com", "mail.com", 
    "tutanota.com", "office365.com", "live.com", "msn.com", "comcast.net", 
    "verizon.net", "att.net", "me.com", "rocketmail.com", "inbox.com"
]

# Check if the email contains '@'
if '@' in email:
    # Find the position of '@' to separate user name and domain
    index = email.index("@")
    
    # Extract the username (text before the '@')
    user_name = email[:index]
    
    # Extract the domain name (text after the '@')
    domain_name = email[index+1:]
    
    # Check if the domain part is valid
    if domain_name in email_domains:
        # Output the username and domain if valid
        print(f"Your user_name is {user_name} and domain is {domain_name}")
    else:
        # Output an error if the domain is not recognized
        print("Invalid domain_name")
else:
    # Prompt user to correct the email if '@' is missing
    print("Enter correct email id...you missed '@'")
