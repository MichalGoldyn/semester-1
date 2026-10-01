"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
from decimal import Decimal
destination = input("Where are you going to? ")
# TODO: convert distance_miles_input and time_hours_input to numbers
try:
    distance_miles_input = int(input("How many miles will you travel? "))
    time_hours_input = int(input("How many hours will the journey take? "))
except:
    print('integers only')


if distance_miles_input <= 0 or time_hours_input <= 0:
    print("You have entered negative or 0 values")


# TODO: calculate the average speed in miles per hour
averageSpeed = Decimal(distance_miles_input/time_hours_input)

correctPrecision = averageSpeed.quantize(Decimal('0.01'))

# TODO: print a summary message using an f-string
print(f'The average speed is {correctPrecision} and the destination is {destination}')
# Extension: add validation for zero or negative values
