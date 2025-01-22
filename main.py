# imports
from reader import *
from datetime import datetime, timedelta
import calendar

# ansii codes
BOLD = "\033[1m"
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

inc = 0
for entry in entries:
    inc = inc + 1
    print("[" + entry[1] + "] " + str(inc) + ". " + YELLOW + entry[0] + RESET + " - " + entry[2])