#!/usr/bin/env python

import getopt
import hashlib
import random
import string
import sys
import time

USAGE_STR = 'writefile.py -n <nelem> -l <lines> -o <outputfile>'
N_ELEM = 20
OUTPUT_FILE = 'output.txt'
N_LINES = 1
ENCODED = False

def main():
    nelem = N_ELEM
    outputfile = OUTPUT_FILE
    nlines = N_LINES
   
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hn:l:o:",["help", "nelem=", "ofile=", "lines="])
    except getopt.GetoptError as err:
        print str(err)
        print USAGE_STR
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print USAGE_STR
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--nelem"):
            nelem = int(arg)
        elif opt in ("-l", "--lines"):
            nlines = int(arg)

    
    writetofile(outputfile, nelem, nlines)

    print "Wrote " + str(nlines) + " lines of " + str(nelem) + " chars to " + outputfile

def writetofile(outputfile, nelem, nlines, encoded = ENCODED):
    f = open(outputfile, 'w')

    for n in range(nlines):
        text = ''
        for n in range(nelem):
            text += random.choice(string.printable[:-5]) #generate printable text (exclude \t\n\r\x0b\x0c)

        length = str(len(text))
        utctime = time.strftime("%d%m%Y:%H%M%S", time.gmtime()) #UTC time, format "ddmmaaaa:HHMMSS"
        shasum = hashlib.sha1(text + utctime).hexdigest()

        result = length + '\t' + text + '\t' + shasum + '\t' + utctime + '\n'
        if encoded:
            result = result.encode("hex")
        f.write(result)


if __name__ == "__main__":
    main()
