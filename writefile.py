#!/usr/bin/env python

import getopt
import hashlib
import random
import string
import sys
import time

USAGE_STR = 'writefile.py -n <nelem> -l <lines> -o <outputfile> --encoded [hex encode output file]'
N_ELEM = 20
OUTPUT_FILE = 'output.txt'
N_LINES = 1

def main():
    nelem = N_ELEM
    outputfile = OUTPUT_FILE
    nlines = N_LINES
    encoded = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hen:l:o:",["help", "encoded", "nelem=", "ofile=", "lines="])
    except getopt.GetoptError as err:
        print str(err)
        print USAGE_STR
        sys.exit(2)

    print "opts", opts
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
        elif opt in ("-e", "--encoded"):
            encoded = True
    
    print "outputfile", outputfile
    print "nelem", nelem
    print "nlines", nlines
    print "encoded", encoded
    
    writetofile(outputfile, nelem, nlines, encoded)

    print "Wrote " + str(nlines) + " lines of " + str(nelem) + " chars to " + outputfile

def writetofile(outputfile, nelem, nlines, encoded):
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
