# Worksheet 1.5: Person class

from datetime import *

class Person:
    """
    A Person, with a name and a date of birth.
    """
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, Name, Birth):
        """Creates an object of Person"""
        self.name = Name
        self.birth = Birth
        if isinstance(self.name, str) != True:
            raise TypeError("name Should be a string")
        else:
            if len(self.name) == 0:
                raise ValueError("Name has to be of a length larger than 0")

        if isinstance(self.birth, date) != True:
            raise TypeError("DOB should be of type date")

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """Returns the initials of names"""
        tmp = self.name.split()
        tmp2 = ""
        for i in tmp:
         tmp2 = tmp2 + i[0]
        return tmp2.upper()

    def is_birthday(self):
        """Return if current day is birthday"""
        current = datetime.now()
        tmp = self.birth
        if tmp.day == current.day and tmp.month == current.month :
            return True
        else:
            return False



