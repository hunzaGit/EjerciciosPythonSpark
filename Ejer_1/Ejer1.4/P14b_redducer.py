#!/usr/bin/python

import sys
import re
import fileinput

dicmovies = dict()
rango = sys.argv[1]
for linea in sys.stdin:
	if linea == "\n":
		continue
	encontrado = linea.find(',"', 0, len(linea))
	if encontrado != -1:
		linea = linea.replace('",', '"//')
		linea = linea.replace(',"', '//"')
		linea= linea.split('//')
	else:
		linea = linea.split(',')
	valoracion = linea[2].split(',')
	if linea[1] in dicmovies:		
		dicmovies[linea[1]][0]=float(dicmovies[linea[1]][0]) + float(valoracion[0])
		dicmovies[linea[1]][1] += 1
	else:
		dicmovies[linea[1]] = [valoracion[0]]
		dicmovies[linea[1]].append(1)
		
for word in dicmovies:
	media = float(dicmovies[word][0])/dicmovies[word][1]
	if media < int(rango) && media >= int(rango)-1:
		print(str(word)+" " +str(media)+"\n")
	