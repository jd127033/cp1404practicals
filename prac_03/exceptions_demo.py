"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When the user input is not a whole number (e.g. a letter, symbol, floating point number etc.)
2. When will a ZeroDivisionError occur?
Answer: when the user tries to input the number 0 as a denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, you can avoid the error by first checking the denominator value before committing to the calculations
"""
# Updated code to prevent ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator can not be 0! Please enter a valid number.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")