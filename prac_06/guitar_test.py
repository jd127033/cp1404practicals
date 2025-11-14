"""
CP1404 Basic Guitar code tester
Start time: 9:30pm
Expected finish time: 9:45pm
Finish time: 9:40pm
"""

from prac_06.guitar import Guitar

# Manually added guitars
gibson = Guitar("Gibson L-5 CES", 1972, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 100)

# Get guitar ages and vintage status
gibson_age = gibson.get_age()
another_guitar_age = another_guitar.get_age()
gibson_vintage_check = gibson.is_vintage()
another_guitar_vintage_check = another_guitar.is_vintage()

# Print Output
print(f"{gibson.name} get_age() - Expected 100 got {gibson_age}")
print(f"{another_guitar.name} get_age() - Expected 9 got {another_guitar_age}")
print(f"{gibson.name} is_vintage() - Expected True. got {gibson_vintage_check}")
print(f"{another_guitar.name} is_vintage() - Expected True. got {another_guitar_vintage_check}")


