"""
CP1404 Practical - guitars
Start time: 10:25pm
Expected Finish time: 11:00pm
Finish time: 11:09pm
"""

from prac_06.guitar import Guitar

def main():
    """ Guitar collection program """
    guitars = [] # Create guitars list
    print("My guitars!")
    name = input("Name: ")
    while name != "": # Ask for new guitars until an empty name is inputted
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_addition = Guitar(name, year, cost) # Create new guitar with inputted info
        guitars.append(guitar_addition) # Add new guitar to guitars list
        print(f"{guitar_addition} added.")
        name = input("Name: ")

    # Add pre-existing guitars
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Check if there are any guitars in the guitars list
    if len(guitars) != 0:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1): # Iterate through each guitar checking vintage status and print out guitar info
            vintage_text = ""
            if guitar.is_vintage():
                vintage_text = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_text}")
    else:
        print("You don't own any guitars. Why not obtain one?")


main()

