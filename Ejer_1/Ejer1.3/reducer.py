#!/usr/bin/python

import sys

# Date  closeValue
# 2017  1046.400024

previous = None
sum = 0
acum = 0

for line in sys.stdin:
        if not line.startswith("Date"):
            anyo, value = line.encode("ascii", "ignore").split( '\t' )
            
            if anyo != previous: # Distinto elemeneto
                if previous is not None: # no es el priemro elemento
                    print previous  + '\t' + str( (sum/acum) ) 
                previous = anyo
                sum = 0
                acum = 0
            
            sum = sum + float( value )
            acum += 1
