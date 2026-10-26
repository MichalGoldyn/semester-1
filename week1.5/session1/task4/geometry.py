# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

from math import *
import point

    
class circle:
    """represent a circle by its radius and its centre coordinates"""

    def __init__(self, aRadius, aCentre):
        self.radius = aRadius
        self.centre = aCentre

    def area(self):
        """return area of circle"""
        tmp = pi * ((self.radius)**2)
        return round(tmp, 4)

    def perimiter(self):
        """Returns area of circumference"""
        tmp = pi * (2*(self.radius))
        return round(tmp, 4)
