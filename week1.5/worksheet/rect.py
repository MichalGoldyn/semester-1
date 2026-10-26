# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """

    def __init__(self, aWidth, aHeight):
            """
                    Creates a Rectangle, given values for width and height.
                    """
            self.width = aWidth
            self.height = aHeight
            if isinstance(aWidth, int) != True or isinstance(aHeight, int) != True:
                raise TypeError("Dimensions should be integers")
            elif aWidth <= 0 or aHeight <= 0:
                raise ValueError("Dimentsions should be larger than or equal to 0")
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
         """Checks for if dimensions object is a square"""
         if self.width == self.height:
              return True
         else:
              return False

    def area(self):
         """Returns area of object"""
         tmp = self.width * self.height
         return tmp

    def perimiter(self):
         """returns the perimiter of the object"""
         tmp = 2*self.width+2*self.height
         return tmp
