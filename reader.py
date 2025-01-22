def read_in(filename):
    f = open(filename)
    lines = f.readlines()

    data = [int(lines[0].replace("\n",""))]
    for line in lines[1:]:
        data.append(line.replace("\n","").split(","))

    return data

def save(filename, tzoffset, entries):
    f = open(filename, "w")
    f.write(
        str(tzoffset) + "\n"
    )
    for entry in entries:
        if len(entry) == 3:
            f.write(
                str(entry[0] + "," + entry[1] + "," + entry[2] + "\n")
            )
        elif len(entry) == 4:
            f.write(
                str(entry[0] + "," + entry[1] + "," + entry[2] + "," + entry[3] + "\n")
            )
    f.close()