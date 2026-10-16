# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = input("Enter name: ")
age = int(input("ENter Age: "))
favCol = input("fav col enter: ")
# Open a file called 'user_info.txt' for reading
with open("week1.3/session2/task3/1_user_info/user_info.txt", "a") as file:
# Write each piece of information to the file, each on a new line.
    file.write(f"{name} \n{age} \n{favCol}\n\n")
# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
