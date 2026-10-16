"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
import time

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
state = "red"
systime = 0

def stateSwticher(indexState, stateList):
        if indexState == (len(stateList)-1):
            return(0)
        else:
            return(indexState + 1)

maxtime = int(input())  # read an integer number of steps (>0)
while systime <= maxtime:
    for x in range(0, states.get(state)):
        print(f"Time {systime:03} State {state}")
        systime += 1
        
    tmp = [x for x in states.keys()]
    stateIndex = tmp.index(state)
    state = tmp[stateSwticher(stateIndex, tmp)]
    











# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14