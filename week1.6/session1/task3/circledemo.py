# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from shapes import *

cir = Circle(2.5, Point(0.0, 0.0)) #Store circle object 

#Outputing Circle details
print(cir)
print(f"Area = {cir.area()}")
print(f"Perimiter = {cir.perimiter()}")

#Changing position of circle obkect
cir.set_position(Point(1.6, 3.2))
print("Moving the circle...")
print(cir)

#Changing coulour of circle object
cir.set_colour("green")
print("Changing the circle's colour...")
print(cir)

