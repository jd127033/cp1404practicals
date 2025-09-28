PASSWORD_LENGTH = 10

""" Password Length Checking Program"""
def main():
    user_password = get_password()
    print_asterisks(user_password)

""" Print asterisks """
def print_asterisks(user_password: str):
    print("*" * len(user_password))

""" Password retrival and check """
def get_password() -> str:
    user_password = (input("Please Enter New Password: "))
    while len(user_password) < PASSWORD_LENGTH:
        print(f"Error: The password must be {PASSWORD_LENGTH} characters long.")
        user_password = (input("Please Enter New Password: "))
    return user_password

main()

