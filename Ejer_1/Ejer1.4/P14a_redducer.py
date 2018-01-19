#!/usr/bin/python
import sys


# in: movieId, title, rating
previousID = None
previousTitle = None
sum = 0
acum = 0

for line in sys.stdin:

    idM, title, rating = line.split( '__' )
    
    if idM != previousID: # Distinto elemeneto
        if previousID is not None: # no es el priemro elemento
            print previousID  + ', ' + previousTitle + ', ' + str( (sum/acum) ) 
        previousID = idM
        previousTitle = title
        sum = 0
        acum = 0
    
    sum = sum + float( rating )
    acum += 1



print previousID  + ', ' + previousTitle + ', ' + str( (sum/acum) )