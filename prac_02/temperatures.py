"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

""" Convert fahrenheit to celsius """
def fahrenheit_to_celsius() -> float:
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

""" Convert celsius to fahrenheit """
def celsius_to_fahrenheit() -> float:
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
