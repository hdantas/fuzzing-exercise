#!/usr/bin/env python

import getopt
import hashlib
import os
import sys
import time

USAGE_STR = 'readfile.py -i <inputfile> --encoded [if input file is encoded]'
INPUT_FILE = 'output.txt'

def main():
    inputfile = INPUT_FILE
    encoded = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hei:",["help", "encoded", "ifile="])
    except getopt.GetoptError as err:
        print str(err)
        print USAGE_STR
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print USAGE_STR
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-e", "--encoded"):
            encoded = True

    print "Reading from " + inputfile
    readfile(inputfile, encoded)
    

def readfile(inputfile, encoded):
    if not os.path.isfile(inputfile):
        print "Can't find file " + inputfile + '\n'
        sys.exit(2)

    f = open(inputfile, 'r')
    lines = f.readlines()
    if encoded:
        lines = lines[0].decode("hex").splitlines()

    for line in lines:

        tokens = line.strip().split('\t') #remove trailing & leading whitespaceand tokenize on \t

        length  = tokens[0]
        text    = tokens[1]
        shasum  = tokens[2]
        utctime = tokens[3]
      
        length_test = length == str(len(text))
        shasum_test = shasum == hashlib.sha1(text + utctime).hexdigest()
        utctime_test = testtime(utctime)

        if not(length_test and shasum_test and utctime_test):
            print "Failed to parse on line '" + line[:-1] + "'"
            sys.exit(2)

    print "Parsed " + inputfile + " correctly!"

def testtime(time_str):
    struct = time.strptime(time_str, "%d%m%Y:%H%M%S")

    length = len(time_str) == 15    
    day    = int(time_str[0:2])   == struct.tm_mday
    month  = int(time_str[2:4])   == struct.tm_mon
    year   = int(time_str[4:8])   == struct.tm_year
    colon  = time_str[8]          == ':'
    hour   = int(time_str[9:11])  == struct.tm_hour
    minute = int(time_str[11:13]) == struct.tm_min
    second = int(time_str[13:15]) == struct.tm_sec

    return length and year and month and day and colon and hour and minute and second


if __name__ == "__main__":
    main()
