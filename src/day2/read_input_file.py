import re


def read(filename):
    '''Reads the file and converts it to an array of objects'''
    array = []
    # https://docs.python.org/3/howto/regex.html
    # https://regex101.com/r/FjWVN6/2
    p = re.compile(
        r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>[a-zA-Z0-9]):\s(?P<password>[a-zA-Z0-9]*)')
    # https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file
    with open(filename, 'r') as reader:
        # Read and print the entire file line by line
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            m = p.match(line)
            array.append(m.groupdict())
            line = reader.readline()

    return array
