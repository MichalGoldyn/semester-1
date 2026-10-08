# Worksheet 1.2: Task 2 Solution
import sys

finished = False
L = []
while finished == False:
    num = float(input("Give float: "))
    L.append(num)
    checkFinished = input("If finished adding values type y otherwise type anythign else: ")
    if checkFinished == "y":
       finished = True


if L == []:
    sys.exit("Error: no numbers provided")
else:
    L.sort()

    listTotal = 0
    listLength = 0
    for i in L:
        listLength += 1
        listTotal += i

    
    print(f"Minimum = {L[0]}")
    print(f"Maximum = {L[listLength - 1]}")
    print(f"Mean = {listTotal/listLength}")
    print(f"Median = {L[listLength // 2]}")