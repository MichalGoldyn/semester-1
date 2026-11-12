# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import point
import geometry

#Data inputs for shape to be created
x = float(input("x: "))
y = float(input("y: "))
r = float(input("radius: "))

cirPos = point.Point(x, y) #Creates the point position where the circles orgin is

cir = geometry.circle(r, cirPos) # Creates the circle object

#Outputs details about the circle object
print(cir.area())
print(cir.perimiter())


    

