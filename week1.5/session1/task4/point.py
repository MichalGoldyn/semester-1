# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """
    

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
    # Add distance() method here
    def distance(self):
        c = round(math.sqrt((self.x)**2 + (self.y)**2), 2)
        print(c)
    # Add distance_to() method here
    def distance_to(self, newX, newY):
        tmpX = self.x - newX
        tmpY = self.y - newY
        c = round(math.sqrt(tmpX**2 + tmpY**2), 2)
        print(c)
    # (This will need a parameter representing another point)


#thing = Point(5,3)
#thing.distance()
#thing.distance_to(1, 2)
# Finally, add code here to demonstrate use of Point
