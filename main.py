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
PURPLE = "\033[35m"

# data assignment
data = read_in("log.txt")
tzoffset = data[0]
mode = data[1]
entries = data[2:]

# set greet phrase
curr = datetime.now()
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
print("The current date is: " + str(datetime.now().strftime("%Y-%m-%d")) + "\n")
print("#################################\n")

user = "init"
entries_curated = []

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
        print(CYAN + "[mode] " + RESET + "\t \t \t toggle modes (week/rolling)")
        print(CYAN + "[add <name> <**limit>]"  + RESET + " \t add a new task (optional time limit in days)")
        print(CYAN + "[check <number>]" + RESET + " \t check off an entry using its number")
        print("\n#################################\n")

    # add new task command
    if user[0:3] == "add":
        user_split = user.split(" ")
        # simple version (1 arg, no time limit)
        if len(user_split) == 2:
            new_entry = [user_split[1], "Incomplete", datetime.utcnow().strftime("%Y-%m-%d"), "No time limit",
                         str(len(entries))]
            entries.append(new_entry)
        # complex version (2 arg, time limit)
        elif len(user_split) == 3:
            new_entry = [user_split[1], "Incomplete", datetime.utcnow().strftime("%Y-%m-%d"), (datetime.utcnow() +
                                                                    timedelta(days=int(user_split[2]))).strftime("%Y-%m-%d"),
                         str(len(entries))]
            entries.append(new_entry)
        # everything else is invalid
        else:
            print("Invalid arguments!")

    if user[0:5] == "check":
        user_split = user.split(" ")
        if len(user_split) == 2:
            entries[int(entries_curated[int(user_split[1]) - 1][4])][1] = "Complete"
        else:
            print("Invalid arguments!")

    if user == "mode":
        if mode == "rolling":
            mode = "week"
            print("Switched to " + CYAN + "[week]" + RESET + " mode")
        elif mode == "week":
            mode = "2week"
            print("Switched to " + CYAN + "[2 week]" + RESET + " mode")
        else:
            mode = "rolling"
            print("Switched to " + CYAN + "[rolling]" + RESET + " mode")

    entries_curated = []
    if mode == "rolling":
        for entry in entries:
            if entry[1] == "Incomplete":
                entries_curated.append(entry)
    elif mode == "week":
        for entry in entries:
            if entry[3] == "No time limit":
                None
            elif datetime.now() + timedelta(days=7) >= datetime.strptime(entry[3], "%Y-%m-%d") >= datetime.now():
                entries_curated.append(entry)
    else:
        for entry in entries:
            if entry[3] == "No time limit":
                None
            elif datetime.now() + timedelta(days=14) >= datetime.strptime(entry[3], "%Y-%m-%d") >= datetime.now():
                entries_curated.append(entry)

    # output tasks every time
    inc = 0
    complete_marker = " "
    entry_color = YELLOW
    for entry in entries_curated:
        if entry[1] == "Complete":
            complete_marker = "X"
        else:
            complete_marker = " "

        if entry[3] =="No time limit":
            entry_color = PURPLE
        else:
            entry_color = YELLOW
        inc = inc + 1
        print("[" + complete_marker + "] " + str(inc) + ". " + entry_color + entry[0] + RESET + " -" +
              " (" + entry[3] + ")")

    user = input("> ")

save("log.txt", tzoffset, mode, entries)
