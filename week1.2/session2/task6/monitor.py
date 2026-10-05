# Week 1.2, Session 2: Task 6
import datetime

machineTemp = int(input("machine temp: "))
machinePSI = int(input("Machine PSI: "))
machineStatus = int(input("Machine Operaional Status: "))
machineUnsafe = False
logFile = open("machine_log.txt", "a")

timestamp = datetime.datetime.now()

logFile.write(timestamp)


if machineTemp > 80:
    print("Temp too high, please shut down")
    machineUnsafe = True
elif machineTemp >=50 and machineTemp <= 80:
    print("Temp is within the safe limits")
elif machineTemp < 50:
    print("Temp is low, no action is needed")

if machinePSI > 100:
    print("Pressure too high, Maintenacne recommended")
    machineUnsafe = True
elif machinePSI >=70 and machinePSI <= 100:
    print("Pressure is stable")
elif machinePSI < 70:
    print("Pressure is low, and is operating normally")

if machineStatus == 1:
    if machineUnsafe == True:
        print("Machine is running unsaftely, Please shut down")
    else:
        print("Machine is running normally")
elif machineStatus == 0:
    print("Machine is not running, no immediate action is needed")
