#!/usr/bin/python

import sys

# Date  massValue
# 1880  21

previous = None
sum = 0
acum = 0

for line in sys.stdin:
    anyo, value = line.encode("ascii", "ignore").split( '\t' )

    if anyo != previous: # Distinto elemento
        if previous is not None: # no es el primer elemento analizado
            print previous  + '\t' + str( (sum/acum) ) 
        previous = anyo
        sum = 0
        acum = 0

    sum = sum + float(value)
    acum += 1


print previous  + '\t' + str( (sum/acum) )