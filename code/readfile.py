#!/usr/bin/env python

import getopt
import hashlib
import os
import sys
import time
import webbrowser
import re

USAGE_STR = 'readfile.py -i <inputfile>'
INPUT_FILE = 'output.txt'

class ReadFile:
    
    LINES_EASTEREGG = 42
    TEXT_EASTEREGG = "PWN1337"
    MAX_TEXT = 1337
    PATTERN = '[A-Z]{2}[A-Za-z][0-9]{3}[A-Za-z0-9]'
    LEN_PATTERN = 7
        

    def readfile(self, inputfile, encoded=True):
        if not os.path.isfile(inputfile):
            print "Can't find file " + inputfile + '\n'
            return

        f = open(inputfile, 'r')
        lines = f.readlines()

        if encoded:
            lines = lines[0].decode("hex").splitlines()

        for line in lines:

            if line.count('\t') != 3:
                print "Failed to parse line '" + line[:-1] + "'"
                return
            
            tokens = line.strip().split('\t') #remove trailing & leading whitespaceand tokenize on \t

            length  = tokens[0]
            text    = tokens[1]
            shasum  = tokens[2]
            utctime = tokens[3]

            if len(length) >= ReadFile.MAX_TEXT or len(text) >= ReadFile.MAX_TEXT or len(shasum) >= ReadFile.MAX_TEXT or len(utctime) >= ReadFile.MAX_TEXT:
                raise Exception('please help...')

            if ReadFile.TEXT_EASTEREGG.find(text) != -1 and len(text) > 0:
                print "Right on! You found an easter egg! You deserve a break."
                webbrowser.open("https://xkcd.com/327/")
                sys.exit(2)

            if ReadFile.LINES_EASTEREGG == len(lines):
                print "Nice! You just found an easter egg!"
                webbrowser.open("https://xkcd.com/571/")
                sys.exit(2)


            length_test = length.isdigit() and length == str(len(text))
            #make sure all the text (in sequences of 7 words) match the regex pattern
            text_test = len(text) == len(re.findall(ReadFile.PATTERN, text)) * ReadFile.LEN_PATTERN
            shasum_test = shasum == hashlib.sha1(text + utctime).hexdigest()
            utctime_test = self.testtime(utctime)

            if not(length_test and text_test and shasum_test and utctime_test):
                print "Failed to parse on line '" + line[:-1] + "'"
                return

        print "Parsed " + inputfile + " correctly!"

    def testtime(self, time_str):
        try:
            struct = time.strptime(time_str, "%d%m%Y:%H%M%S")
        except:
            return False

        length = len(time_str) == 15    
        day    = int(time_str[0:2])   == struct.tm_mday
        month  = int(time_str[2:4])   == struct.tm_mon
        year   = int(time_str[4:8])   == struct.tm_year
        colon  = time_str[8]          == ':'
        hour   = int(time_str[9:11])  == struct.tm_hour
        minute = int(time_str[11:13]) == struct.tm_min
        second = int(time_str[13:15]) == struct.tm_sec

        return length and year and month and day and colon and hour and minute and second


def main():
    inputfile = INPUT_FILE
    encoded = True

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
            encoded = not encoded

    print "Reading from " + inputfile

    newfile = ReadFile()
    newfile.readfile(inputfile, encoded)

if __name__ == "__main__":
    main()