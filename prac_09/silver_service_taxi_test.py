"""
CP1404/CP5632 Practical
Silver Service Taxi Test
Estimated finish: 20 min
Finish: 10 min
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """SilverServiceTaxi Class Test"""
    new_taxi = SilverServiceTaxi("Fancy Cab", 100, 2)
    new_taxi.drive(18)
    print(new_taxi.get_fare())
    print(new_taxi)
    assert new_taxi.get_fare() == 48.80


main()
