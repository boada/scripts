#!/usr/bin/python
import sys
import numpy as np
def filter_finder(filter, filter_file):
    '''This finds and returns filter data from a large filter file.

    The data should be formatted as follows. 
    <Size of filter> <Filter Name>
    [ [Index] [Wavelength] [Transmission]
            ...
            ...
        [Index] [Wavelength] [Transmission] ]'''

    data = []
    with open(filter_file,"rt") as file:
        for num, line in enumerate(file,1):
            if filter in line:
                index = num
                print line.strip('\n')
                line_info = line.split()
                found = True
                break
            else:
                found = False
    if not found:
        print "Filter '%s' not found!" % (filter)
        return 0
    else:
        with open(filter_file,"rt") as file:
            for num, line in enumerate(file,1):
                if num > index and num <= index +int(line_info[0]):
                    data.append(line.split())

    return data

if __name__ == "__main__":
    sys.exit(filter_finder(sys.argv[1],sys.argv[2]))

