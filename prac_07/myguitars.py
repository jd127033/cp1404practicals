"""
CP1404 Practical - My Guitars program.
Start time: 11:04
expected finsh: 25 min
finish  min
"""
from guitar import Guitar


def main():
    """Read guitars from file, sort by year, and display sorted list."""
    guitars = load_guitars('guitars.csv')

    # Print original all guitars
    print("All guitars:")
    display_guitars(guitars)

    # Sort guitars (oldest to newest)
    guitars.sort()

    print("Sorted Guitars by year (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from CSV and return a list of guitars."""
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


if __name__ == '__main__':
    main()