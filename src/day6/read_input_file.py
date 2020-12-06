def read(filename):
    '''Reads the file and converts it to an array of objects'''
    array = []
    group = []
    # https://stackoverflow.com/questions/15599639/what-is-the-perfect-counterpart-in-python-for-while-not-eof
    with open(filename, 'r') as reader:
        # Read and print the entire file line by line
        while line := reader.readline():
            line = line.strip("\n")
            if (line == ''):
                array.append(group)
                group = []
            else:
                group.append(line)
        if (len(group) != 0):
            array.append(group)

    return array
