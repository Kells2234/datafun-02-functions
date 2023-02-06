"""
Kelly Simmons
1/30/2023
Data Analytics Fundamentals
Project 2

This script will define a PyBuddy class that describes the 2022 season statistics of a single NASCAR Driver
The drivers statistics include these attributes:
    Heat Race___________string, selected at random from a list
    top 5 finishers__________int
    
"""

# import from dataclasses to make our job even easier
from dataclasses import dataclass, field

import datetime
from enum import Enum


class Heat(Enum):
    Heat_1 = 1
    Heat_2 = 2
    Heat_3 = 3
    Heat_4 = 4


# Add the @dataclass decorator to let Python do more of the work
# Notice what changes.


@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy."""

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Clash"
    heat_number: int = 1
    car_number: int = 4
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I provide the top 5 winners of each heat race"
        else:
            return ""

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy.
{self.to_string()}
You'll need curiousity, the ability to search the web, 
and the tenacity and resourcefulness
to solve all kinds of challenges.
Let's get started! 

        """
        )

    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
I'm a {self.heat} with {self.car_numbers} legs.
In finished my heat in {self.finishing_postion()}.
I know:
{self.get_skills_string()}
"""


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run, do this:
if __name__ == "__main__":

    # Create an instance of a PyBuddy
    dale = PyBuddy(
        "Dale",
        heat_number = 1,
        car_number = 3,
        finishing_position = 4,
        [car_number advances to the feature race],
    )

    # Call the buddy's welcome() method
    dale.display_welcome()

    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    Bubba = PyBuddy(
        name="Bubba",
        heat_number = 2
        car_number = 23
        finishing_position = 2
        is_available=True,
        [Driver advnces to the feature race],
    )

    Bubba.display_welcome()
