#!/usr/bin/env python

import getopt
import hashlib
import os
import sys
import time

USAGE_STR = 'readfile.py -i <inputfile>'
INPUT_FILE = 'output.txt'

def main():
    inputfile = INPUT_FILE
   
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:",["help", "ifile="])
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

    print "Reading from " + inputfile
    readfile(inputfile)
    

def readfile(inputfile):


    if not os.path.isfile(inputfile):
        err = "Can't find file " + inputfile + '\n'
        print str(err)
        sys.exit(2)

    f = open(inputfile, 'r')
    
    for line in f.readlines():

        tokens = line[:-1].split('\t') #remove \n from end of line and tokenize on \t

        length  = tokens[0]
        text    = tokens[1]
        shasum  = tokens[2]
        utctime = tokens[3]
      
        length_test = length == str(len(text))
        shasum_test = shasum == hashlib.sha1(text).hexdigest()
        utctime_test = type(time.strptime(utctime, "%d%m%Y:%H%M%S")) == time.struct_time

        if not(length_test and shasum_test and utctime_test):
            print "Failed to parse on line '" + line[:-1] + "'"
            sys.exit(2)

    print "Parsed " + inputfile + " correctly!"

if __name__ == "__main__":
    main()
