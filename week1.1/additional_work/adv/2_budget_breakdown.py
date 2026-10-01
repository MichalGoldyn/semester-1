"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""
from decimal import Decimal
try:
    travel_cost_input = Decimal(float(input("Travel cost in pounds: "))).quantize(Decimal('0.01'))
    food_cost_input = Decimal(float(input("Food cost in pounds: "))).quantize(Decimal('0.01'))
    accommodation_cost_input = Decimal(float(input("Accommodation cost in pounds: "))).quantize(Decimal('0.01'))
except:
    print('Please Enter numbers only')

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places

totalSpend = Decimal(travel_cost_input + food_cost_input + accommodation_cost_input).quantize(Decimal('0.01'))
averageSpend = Decimal(totalSpend / 3).quantize(Decimal('0.01'))


print(f'The total spend is {totalSpend}, the average spend is {averageSpend}, the cost of travel is {travel_cost_input}, the cost of food is {food_cost_input}, the cost of accomodation is {accommodation_cost_input}')