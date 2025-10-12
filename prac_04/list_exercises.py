""" Number checking program """

REQUIRED_AMOUNT_OF_NUMBERS = 5
number_count = 0
number_list = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

while number_count < REQUIRED_AMOUNT_OF_NUMBERS:
    number = int(input("Number: "))
    number_list.append(number)
    number_count += 1

# Use inbuilt functions to determine special numbers
smallest_number = min(number_list)
largest_number = max(number_list)
average_number = sum(number_list)/len(number_list)

print(f"The first number is {number_list[0]}")
print(f"The last number is {number_list[-1]}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average_number}")

""" Password checker program """
guess = input("What is your username? ")
password_check = 0
while password_check == 0:
    if guess in usernames:
        password_check = 1
        print("Access Granted.")
    else:
        print("Access Denied")
        guess = input("What is your username? ")

