def read_in(filename):
    f = open(filename)
    lines = f.readlines()

    data = [int(lines[0].replace("\n",""))]
    for line in lines[1:]:
        data.append(line.replace("\n","").split(","))

    return data