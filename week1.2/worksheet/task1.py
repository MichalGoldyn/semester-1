# Worksheet 1.2: Task 1 Solution
import sys

try:
    num = int(input("Integer between 0 - 100: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if num < 40 and num >= 0:
    print(f"{num} is a Fail")
elif num >= 40 and num <=69:
    print(f"{num} is a Pass")
elif num >= 70 and num <= 100:
    print(f"{num} is a Distinction")
else:
    sys.exit('Error: Grade must be an integer between 0 and 100')
