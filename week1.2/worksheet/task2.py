from util import read_numbers
import sys

L = read_numbers()

if L == []:
    sys.exit("Error: no numbers provided")
else:
    L.sort()

    listTotal = sum(L)
    listLength = len(L)
    
    print(f"Minimum = {L[0]}")
    print(f"Maximum = {L[listLength - 1]}")
    print(f"Mean = {listTotal/listLength}")
    if listLength % 2 != 0:
        print(f"Median = {L[listLength // 2]}")
    else:
        print(f"Median = {(L[listLength // 2] + L[(listLength // 2)-1])/2}")