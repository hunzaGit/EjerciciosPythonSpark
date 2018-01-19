#!/usr/bin/python
import sys

rango = sys.argv[1]


def imprimirresult(idM, titulo, media):
	if media <= int(rango) and media > int(rango)-1:
		print(str(idM) + ", " + titulo + ", " + str(media))

# in: movieId, title, rating
previousID = None
previousTitle = None
sum = 0
acum = 0

for line in sys.stdin:

    idM, title, rating = line.split( '__' )
    
    if idM != previousID: # Distinto elemeneto
        if previousID is not None: # no es el priemro elemento
            imprimirresult(previousID, previousTitle, (sum/acum) ) 
        previousID = idM
        previousTitle = title
        sum = 0
        acum = 0
    
    sum = sum + float( rating )
    acum += 1



imprimirresult(previousID, previousTitle, (sum/acum) ) 