# imports
from reader import *
from datetime import datetime, timedelta
import calendar

# ansii codes
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"
YELLOW = "\033[33m"

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

user = ""

while user is not "q":

    if user.lower() == "help" or user.lower() == "man" or user.lower() == "h" or user.lower() == "docs":
        for i in range(20):
            print("\n")
        print("######## VALID COMMANDS! ########\n")
        print("[q] - quit EASY PLANNER")
        print("\n#################################\n")

    inc = 0
    complete_marker = " "
    for entry in entries:
        if entry[1] == "Complete":
            complete_marker = "X"
        else:
            complete_marker = " "
        inc = inc + 1
        print("[" + complete_marker + "] " + str(inc) + ". " + YELLOW + entry[0] + RESET + " - " + entry[2])

    user = input("" + BLINK + "> " + RESET)