"""
CP1404/CP5632 Practical
Band class
Estimated Time: 20 min
Finish Time : 15 min
"""


class Band:
    """Band class - represents band of musicians."""

    def __init__(self, name=""):
        """Construct Band with empty musician collection and a name."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of a Band."""
        musicians_str = ", ".join(
            str(musician) for musician in self.musicians)  # Format musician string to match output.
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Return string showing each musician playing their first or lack of instrument."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)

    def add(self, musician):
        """Add musician to bands collection."""
        self.musicians.append(musician)
