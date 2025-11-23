"""
CP1404/CP5632 Practical
Car class
Estimated finish: 20 min
Finish: 20 min
"""
from prac_09.car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability rating."""
        return f"{super().__str__()}, {self.name} has a reliability rating of {self.reliability}."

    def drive(self, distance):
        """Drive like parent Car only has a chance to drive with likelihood depending on reliability value."""
        drive_probability = random.randint(0, 100)
        if drive_probability < self.reliability:
            distance_driven = super().drive(distance)
            print(f"The car travelled {distance_driven} kilometre!\n")
        else:
            distance_driven = 0
            print(f"The car wouldn't go!\n")
        return distance_driven

