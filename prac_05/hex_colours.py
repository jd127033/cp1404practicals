"""
CP1404/CP5632 Practical
Colours in a dictionary
"""
#Dictionary of colours
CODE_TO_COLOUR = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "AMBER": "#ffbf00", "AMETHYST": "#9966cc",
                  "AQUA": "#fbceb1", "ASPARAGUS": "#87a96b", "AUREOLIN": "#fdee00", "BABY BLUE": "#89cff0"}

#Ask for input until empty input is entered, return the code for the entered colour
colour_code = input("Enter colour name: ").upper()
while colour_code != "":
    try:
        print(colour_code, "is code", CODE_TO_COLOUR[colour_code])
#KeyError Occurs when an attempt to access a key in a dictionary fails
    except KeyError:
        print("Invalid Colour")
    colour_code = input("Enter colour name: ").upper()