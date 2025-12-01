"""
Prac 09 task - Unreliable car test
Overview: Test Unreliable car class
Estimated finish: 20 min
Finish: 20 min
"""

from prac_09.taxi import Taxi
from prac_09.unreliable_car import UnreliableCar

successful_attempts = 0

unreliable_car = UnreliableCar("Captiva", 100, 30)
# Attempt to drive Captiva 100 times then relay amount of successful attempts.
for i in range(100):
    print(f"Attempt {i}: Starting Car...")
    distance_driven = unreliable_car.drive(1)
    if distance_driven > 0:
        successful_attempts += 1

print(f"{unreliable_car.name} successfully drove {successful_attempts} times!")
