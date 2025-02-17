#!/usr/bin/env python3
# Author ID: ssharma608

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        if type(number1) == str:
            number1 = int(number1)

        if type(number2) == str:
            number2 = int(number2)       

        add = number1 + number2
        return add

    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')  # Open the file in read mode
        lines = f.readlines()    # Read all lines from the file
        f.close()                # Close the file after reading
        return lines
    except (FileNotFoundError, PermissionError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
