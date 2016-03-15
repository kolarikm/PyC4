#!/usr/bin/env python
import sys, getopt

#Default board dimensions
width=10
height=10
length=4

#Attempt to read 3 command line arguments -w for width, -h for height, and -l for length
try:
    myopts, args = getopt.getopt(sys.argv[1:],"w:h:l:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -w width -h height -l length" % sys.argv[0])
    sys.exit(2)

#Assign arguments to variables if they are integers, exit it not
for opt, arg in myopts:
    if opt == '-w':
        try:
            width = int(arg)
        except ValueError:
            print "Board dimensions must be integers"
            sys.exit(2)
    elif opt == '-h':
        try:
            height = int(arg)
        except ValueError:
            print "Board dimensions must be integers"
            sys.exit(2)
    elif opt == '-l':
        try:
            length = int(arg)
        except ValueError:
            print "Board dimensions must be integers"
            sys.exit(2)

print ("Width : %s  Height: %s  Length: %s" % (width, height, length))
if isinstance(width, int):
    print "Width is an integer!"
