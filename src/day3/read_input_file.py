def read(filename):
    '''Reads the file and converts it to an array of objects'''
    array = []
    # https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file
    with open(filename, 'r') as reader:
        # Read and print the entire file line by line
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            array.append(line.strip("\n"))
            line = reader.readline()

    return array
