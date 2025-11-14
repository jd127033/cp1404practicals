"""
CP1404 Practical - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car",180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create limo with Car class, add fuel and drive
    my_limo = Car("Limo", 100)
    my_limo.add_fuel(20)
    print(f"Limo has fuel: {my_limo.fuel}")
    my_limo.drive(115)
    print(my_limo)




main()
