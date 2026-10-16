# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.
from pprint import pprint

# open and read the file
with open('week1.3/session2/task2/2_log_data/site.log', 'r') as file:
# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20
    Data = [x.split() for x in file]

    for f in Data:
        if f[4] == '"POST' and f[5] == '/login"' and f[6] == '401':
            print(f"IP address {f[2]} failed to login at {f[1]} on {f[0]}")
# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data