from reader import save
from datetime import *

def dump(dest, tzoffset, mode, entries):
    finished_entries = []
    ongoing_entries = []
    index = 0
    for entry in entries:
        if entry[3] == "No time limit":
            if entry[1] == "Complete":
                finished_entries.append(entry)
        elif datetime.now() > datetime.strptime(entry[3], "%Y-%m-%d"):
            finished_entries.append(entry)
        else:
            ongoing_entries.append(entry)
            ongoing_entries[index][4] = str(index)
            index += 1

    save("old/" + dest, tzoffset, mode, finished_entries)
    return ongoing_entries