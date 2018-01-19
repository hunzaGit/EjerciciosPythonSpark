#!/usr/bin/python

import sys
import re
import fileinput

dicmovies = dict()

for line in sys.stdin:
	encontrado = linea.find(',"', 0, len(linea))
	if encontrado != -1:
		linea = linea.replace('",', '"//')
		linea = linea.replace(',"', '//"')
		linea= linea.split('//')
	else:
		linea = linea.split(',')
	if linea[1] in dicmovies:		
		dicmovies[linea[1]][0]=dicmovies[linea[1]][0] + linea[2]
		dicmovies[linea[1]][1] += 1
	else:
		dicmovies[linea[1]] = [linea[2]]
		dicmovies[linea[1]].append(1])
		
for word in dicmovies:
	media = dicmovies[word][0]/dicmovies[word][1]
    print(word+" " +str(media)+"\n")
	