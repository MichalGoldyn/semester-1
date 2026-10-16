# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("week1.3/session2/task3/2_average_grade/student_data.csv", "r") as data:
# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
    gradeData = [x.rstrip("\n").split(",") for x in data]
    for i in range(1, len(gradeData)-1):
        tmp = int(gradeData[i][2]) + int(gradeData[i][3]) + int(gradeData[i][4])
        tmp2 = round((tmp/3), 2)
        print(tmp2)
        with open("week1.3/session2/task3/2_average_grade/report.txt", "a") as report:
            report.write(f"{gradeData[i][1]}: {tmp2} \n")

# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
