"""
Kelly Simmons
1/30/2023
Data Analytics Fundamentals
Project 2

This script will define a PyBuddy class that describes the 2022 season statistics of a single NASCAR Driver
The drivers statistics include these attributes:
    race team___________string, selected at random from a list
    car number__________int
    races run___________int
    finishing positions_________int
    best finishes___________int
    average finishing postiion_________float (finishing positions / races)
"""

# first, import helpful modules to make our job easier

import datetime
from enum import Enum


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4

# define class that contains different racing series
class "level"(Enum):
    CUP level = 1
    Xfinity level = 2
    Craftsman level = 3

# instantiate the list of teams
teams = (
    ('23XI Racing'),
    ('Frontrow Motorsports')
    ('Hendrick Motorsports')
    ('JD Motorsports')
    ("Joe Gibbs Racing")
    ('JR Motorsports')
    ('JTG Daugherty Racing')
    ('Kaulig Racing')
    ('Kyle Busch Motorsports')
    ('Live Fast Motorsports')
    ('MBM Motorsports')
    ('Niece Motorsports')
    ('Petty GMS Motorsports')
    ('RFK Racing')
    ('Richard Childress Racing')
    ('Rick Ware Racing')
    ('Spire Motorsports')
    ('Stewart Hass Racing')
    ('Thorsport Racing')
    ('Trackhouse Racing')
    ('Wood Brothers Racing')
)

def populate_list_of_Cars():
    #initiate an empty list to be populated
    car_numbers = []

    for i in range(36):
        populate_list_of_cars.append(random.randint(0,4))

    populate_list_of_cars = (
      ('23', '45')
      ('34', '38')
      ('5', '9', '24', '48') 
      ('11', '19', '20', '54')
      ('47')
      ('16', '31')
      ('78') 
      ('66', '55')
      ('43', '42')
      ('6', '17')
      ('8', '3')
      ('51')
      ('7', '77')
      ('4', '10', '14')
      ('2', '12', '22')
      ('1', '99')
      ('21')
    )

def races_run():
    return random.randint(1, 36)


#add in fileds that represent the driver stats
self.driver_name = "Joey Lagano"

self.team = teams[random.randint(0, 38)]

#choose a level at random
self.level = Level.value = random.randint(1, 3)

# populate a list that represents finishing position by the driver, one entry per race
# list is populate by populate finishing_position 
class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, species, num_legs, weight_kgs, is_available, skill_list):
        """ Built-in method to create a new instance."""
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.weight_kgs = weight_kgs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"

        if self.is_available:
            s4 = "I'm available for tutoring.\n"
        else:
            s4 = "I'm already helping others learn Python.\n"

        s5 = "I know:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())

        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "Alice",
        Species.CAT,
        4,
        8.123456,
        True,
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    # Call the buddy's welcome() method
    alice.display_welcome()


    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Rex",
        species=Species.DOG,
        num_legs=4,
        weight_kgs=10.437241,
        is_available=True,
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    rex.display_welcome()
