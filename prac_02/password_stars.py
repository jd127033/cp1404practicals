""" Password Length Checking Program"""

PASSWORD_LENGTH = 10

user_password = (input("Please Enter New Password: "))
while len(user_password) < PASSWORD_LENGTH:
    print(f"Error: The password must be {PASSWORD_LENGTH} characters long.")
    user_password = (input("Please Enter New Password: "))
print("*" * len(user_password))

