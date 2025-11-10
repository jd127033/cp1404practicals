"""CP1404 Practical - Guitar class."""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.
        Year: The year the guitar was made
        Cost: Price of Guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ String representation of Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculates the age of the guitar with a reference year of 2022"""
        age = int(2022 - self.year)
        return age

    def is_vintage(self):
        """Checks if guitar is vintage by checking if age is 50 years or older"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return comparison based on year"""
        return self.year < other.year
