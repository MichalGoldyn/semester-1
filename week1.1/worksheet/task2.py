"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

from decimal import Decimal
try:
    monthlySavings = float(input())
    annualSavings = monthlySavings * 12
    finalSavedAmount = annualSavings * (1 + 0.008)
    precisionAmount = Decimal(str(finalSavedAmount))
    finalAmount = precisionAmount.quantize(Decimal("0.01"))

    print(round(annualSavings))
    print("£" + str(finalAmount))

except:
    print("Invalid amount")


#### I didn't have this template originally so man it took me a bit to realise the autograder was inputing a name before inputing actual values into the calc