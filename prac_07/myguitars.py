"""
CP1404 Practical - My Guitars program.
Start time: 11:04
expected finsh: 25 min
finish 20 min
"""
from guitar import Guitar


def main():
    """Read guitars from file, sort by year, and display sorted list. Also ask for new guitars and save to csv"""
    guitars = load_guitars('guitars.csv')

    # Add new guitars
    print("Add your new guitars (leave name blank to finish)")
    add_guitars(guitars)

    # Save guitars to file
    save_guitars('guitars.csv', guitars)
    print(f"{len(guitars)} guitars saved to guitars.csv")

    # Print original guitars
    print("")
    print("All guitars:")
    display_guitars(guitars)

    # Sort guitars (oldest to newest)
    guitars.sort()
    print("")
    print("Sorted Guitars by year (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from guitars.csv and return a list of guitars."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display guitars in the list."""
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars):
    """Prompt to add new guitars to the list until blank is added"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        added_guitar = Guitar(name, year, cost)
        guitars.append(added_guitar)
        print(f"{added_guitar} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars to guitars file."""
    with open(filename, 'w') as file: # Rewrite CSV file for each run through of code so that guitars don't duplicate
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == '__main__':
    main()