#!/usr/bin/python

import sys

# palabra   1 
previous = None
sum = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous: #elemento distinto
        if previous is not None: # Primer elemento
            print str( sum ) + '\t' + previous
        previous = key
        sum = 0
    
    sum = sum + int( value )

print str( sum ) + '\t' + previous
