# Week 1.2, Session 2: Task 6
import datetime

machineTemp = int(input("machine temp: "))
machinePSI = int(input("Machine PSI: "))
machineStatus = int(input("Machine Operaional Status: "))
machineUnsafe = False
logFile = open("machine_log.txt", "a")

timestamp = str(datetime.datetime.now())

logFile.write("\n\n" + timestamp + "\n\n")

if machineTemp > 80:
    print("Temp too high, please shut down")
    logFile.write("Temp too high, please shut down\n")
    machineUnsafe = True
elif machineTemp >=50 and machineTemp <= 80:
    print("Temp is within the safe limits")
    logFile.write("Temp is within the safe limits\n")
elif machineTemp < 50:
    print("Temp is low, no action is needed")
    logFile.write("Temp is low, no action is needed\n")

if machinePSI > 100:
    print("Pressure too high, Maintenacne recommended")
    machineUnsafe = True
    logFile.write("Pressure too high, Maintenacne recommended\n")
elif machinePSI >=70 and machinePSI <= 100:
    print("Pressure is stable")
    logFile.write("Pressure is stable\n")
elif machinePSI < 70:
    print("Pressure is low, and is operating normally")
    logFile.write("Pressure is low, and is operating normally\n")

if machineStatus == 1:
    if machineUnsafe == True:
        print("Machine is running unsaftely, Please shut down")
        logFile.write("Machine is running unsaftely, Please shut down\n")
    else:
        print("Machine is running normally")
        logFile.write("Machine is running normally\n")
elif machineStatus == 0:
    print("Machine is not running, no immediate action is needed")
    logFile.write("Machine is not running, no immediate action is needed\n")
