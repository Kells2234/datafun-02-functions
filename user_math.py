"""
Kelly Simmons
January 25, 2023
Always start with a docstring that describes what the module does.

The goal of this project is to write custom functions using concept learned in chapters 3 and 4

"""

import math
from socket import if_nameindex

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None
   


# define more functions here (see instuctions)


def get_total_car_count (number_of_cars):
    """
    Returns a count of the number of cars to finish a race.

    """
    try:
        if(len(number_of_cars) == 36):
            return 36
        else:
            return math.fsum(number_of_cars)
    except Exception as ex:
        print(f"Error: {ex}")
        return None

def calculate_finishing_average(finishing_position, races):
    """
    Return a float value equal to finishing position / races to show the drivers average finishing position over a season
    """
    try:

        average_finishing_postion = float(finishing_position / races)

        if(average_finishing_postion <= 7):
            print("Driver is elite")

        return average_finishing_postion
    except ZeroDivisionError as ex:
        print("Error: Cannot divide by zero")
        return None 

def merch_plus_tax(unit_price, tax_rate):
    """
    This function calculates the total cost of an item after adding sales tax
    The first value is the unit_price which represents the cost  item before tax
    The second value is tax_rate which represents the tax that is to be added to the price
    """
    try:
        return unit_price + (unit_price * tax_rate)
    except Exception as ex:
        print(f"Error: {ex}")
        return None





# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"math.comb(5,3) = {math.comb(5,3)}")
    print(f"math.perm(5,3) = {math.perm(5,3)}")
    print()
    print(f"math.pi = {math.pi}")
    print()
    print()
    print(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    print(f"math.radians(180)         = {math.radians(180)}")
    print()
    print(f"get_area_of_lot(5, 10) = {get_area_of_lot(5, 10)}")
    print(f"get_area_of_lot(-16, 2) = {get_area_of_lot(-16.3, 2.5)}")
    print(f"get_area_of_lot(math.inf, 1) = {get_area_of_lot(math.inf, 1)}")
    print(f"get_area_of_lot('five', 'three') = {get_area_of_lot('five', 'three')}")
    print()
    print("Call get_total_car_count() with several arguments")
    print(f"get_total_car_count([36,39,37,40,43,34]) = {get_total_car_count([36,39,37,40,43,34])}")
    print(f"get_total_car_count[5] =") # all cars finished the race
    print(f"get_total_car_count[6] =") # depending on the track there were a lot of wreck or one big wreck
    print(f"get_total_car_count[36,40] =") # there were some wrecks but none were major
    print()
    print("Call calculate_finishing_average() with a few arguments")
    print()
    print(f"calculate_finishing_average([5,10,17,3,1,1,4]) = {calculate_finishing_average([5,10,17,3,1,1,4])}")
    print(f"calculate_finishing_average = [5,10,17,3,1,1,4] / 7")
    print(f"Call calculate_finishing_average")
    print()
    print("Call merch_plus_tax")
    print()
    print(f"merch_plus_tax(100, 0.07) = {merch_plus_tax(75, 0.07)}")
    print(f"merch_plus_tax(100, math.inf) = {merch_plus_tax(100, math.inf)}")
    print(f"merch_plus_tax(100, 0) = {merch_plus_tax(100, 0)}")



