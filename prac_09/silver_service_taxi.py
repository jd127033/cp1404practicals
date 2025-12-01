"""
CP1404/CP5632 Practical
Silver Service Taxi class
Estimated finish: 20 min
Finish: 30 min
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a Silver Service Taxi instance, based on the parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a taxi but with additional flagfall info."""
        return f"{super().__str__()}, ${self.price_per_km} plus flagfall of ${self.flagfall:.2f}."

    def get_fare(self):
        """Return price for taxi trip including flagfall fee."""
        return super().get_fare() + self.flagfall
