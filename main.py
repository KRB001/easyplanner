# imports
from reader import *
from datetime import datetime, timedelta
import calendar

# ansii codes
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# data assignment
data = read_in("log.txt")
tzoffset = data[0]
entries = data[1:]

# set greet phrase
curr = datetime.utcnow() + timedelta(hours=tzoffset)
time_of_day = ""
if 0 <= curr.hour < 12:
    time_of_day = "morning"
elif 12 <= curr.hour < 17:
    time_of_day = "afternoon"
else:
    time_of_day = "evening"

# header
for i in range(20):
    print("\n")
print("#### WELCOME TO EASY PLANNER ####\n")
print("Good " + time_of_day + "! Your tasks are listed below.\n")
print("#################################\n")

user = "init"

# input loop
while user is not "q":

    if user is not "init":
        for i in range(20):
            print("\n")

    # user help command
    if user.lower() == "help" or user.lower() == "man" or user.lower() == "h" or user.lower() == "docs":
        for i in range(20):
            print("\n")
        print("######## VALID COMMANDS! ########\n")
        print(CYAN + "[q] " + RESET + "\t \t \t quit EASY PLANNER")
        print(CYAN + "[add <name> <**limit>]"  + RESET + " \t add a new task (optional time limit in days)")
        print("\n#################################\n")

    # add new task command
    if user[0:3] == "add":
        user_split = user.split(" ")
        # simple version (1 arg, no time limit)
        if len(user_split) == 2:
            new_entry = [user_split[1], "Incomplete", str(datetime.utcnow()), "No time limit"]
            entries.append(new_entry)
        # complex version (2 arg, time limit)
        elif len(user_split) == 3:
            new_entry = [user_split[1], "Incomplete", str(datetime.utcnow()), str(datetime.utcnow() +
                                                                    timedelta(days=int(user_split[2])))]
            entries.append(new_entry)
        # everything else is invalid
        else:
            print("Invalid arguments!")

    # output tasks every time
    inc = 0
    complete_marker = " "
    for entry in entries:
        if entry[1] == "Complete":
            complete_marker = "X"
        else:
            complete_marker = " "
        inc = inc + 1
        print("[" + complete_marker + "] " + str(inc) + ". " + YELLOW + entry[0] + RESET + " - " + entry[2] +
              " (" + entry[3] + ")")

    user = input("> ")

save("log.txt", tzoffset, entries)