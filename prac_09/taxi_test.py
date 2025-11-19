"""
Prac 09 task - Taxi test
Overview: Test taxi class
Estimated finish: 20 min
Finish: 20 min
"""

from prac_09.taxi import Taxi

new_taxi=Taxi("Prius 1", 100)
new_taxi.drive(40)
print(new_taxi)
print(f"The current fare for the new taxi is ${new_taxi.get_fare()}\n")
new_taxi.start_fare()
new_taxi.drive(100)
print(new_taxi)
print(f"The current fare for the new taxi is ${new_taxi.get_fare()}")






