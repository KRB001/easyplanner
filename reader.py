def read_in(filename):
    f = open(filename)
    lines = f.readlines()

    data = []
    for line in lines:
        data.append(line.replace("\n","").split(","))

    return data