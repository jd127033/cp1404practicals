"""
CP1404 Practical - Programming language class.
Start time: 2:20am
Expected Finish time: 2:35am
Finish time: 2:45am
"""

class ProgrammingLanguage:
    """Represent a Programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Checks if the language is dynamic or not returning a boolean value"""
        return self.typing == "Dynamic"
