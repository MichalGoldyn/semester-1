import random

# Read names from a file

with open("week1.8/session1/task1-random/names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("Ran num: "))
nameList = []
for name in range(num):
    randomName = random.choice(names)
    if randomName in nameList:
        randomName = random.choice(names)
    else:
        nameList.append(randomName)

for i in nameList:
    print(i)
    
# Display the chosen names, one per line
