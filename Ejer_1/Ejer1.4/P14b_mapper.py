#!/usr/bin/python

import sys
import re
import fileinput

movies = sys.argv[1]
ratings = sys.argv[2]
dicmovies = dict()
for linea in fileinput.input(movies):
    if not fileinput.isfirstline():
		encontrado = linea.find(',"', 0, len(linea))
		if encontrado != -1:
			linea = linea.replace('",', '"//')
			linea = linea.replace(',"', '//"')
			linea= linea.split('//')
		else:
			linea = linea.split(',')
		if linea[0] in dicmovies:
			dicmovies[linea[0]].append(linea[1],linea[2])
		else:
			dicmovies[linea[0]] = [linea[1],linea[2]]
			
for linea in fileinput.input(ratings):
    if not fileinput.isfirstline():
		linea = linea.split(',')
		linea[1]=dicmovies[linea[1]][0]
		print(str(linea[0])+','+str(linea[1])+','+str(linea[2])+','+str(linea[3]))