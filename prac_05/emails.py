"""
CP1404/CP5632 Practical
Emails using dictionaries
estimate: 30 min
actual:  30 min
"""

# Create directory for email to name
email_to_name = {}
# Ask for user email
email = input("Email: ")
while email != "":
    # Break down email into parts
    assumed_name = email.split('@')[0]
    pieces = assumed_name.split('.')
    name = " ".join(pieces).title()
    # Confirm name with user
    confirm_name = input(f"Is your name {name}? (Y/n) ")
    # If user doesn't confirm name, ask for their name.
    if confirm_name.upper() != "Y" and confirm_name != "":
        name = input("Name: ")
    # Assign name to email
    email_to_name[email] = name
    email = input("Email: ")

# Print emails with associated names
for email, name in email_to_name.items():
    print(f"{name} ({email})")
