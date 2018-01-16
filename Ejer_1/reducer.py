#!/usr/bin/python

import sys

# Date  closeValue
# 2017-12-29  1046.400024




previous = None
sum = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print str( sum ) + '\t' + previous
        previous = key
        sum = 0
    
    sum = sum + int( value )

print str( sum ) + '\t' + previous
