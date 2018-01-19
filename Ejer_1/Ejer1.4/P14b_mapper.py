#!/usr/bin/python

import sys
import re
import fileinput

movies = sys.argv[1]
ratings = sys.argv[2]
dicmovies = dict()


# Dos tipos distintos
# ['39,Clueless (1995),Comedy|Romance']
# ['40,' , 'Cry, the Beloved Country (1995)' , ',Drama']
def formatearTitulo(line):
	if len(line) == 1:
		line = line[0].split(',')
	if len(line) >= 1:
		id = line[0].split(',')[0]
	return (id, line[1])


# in: movieId,title,genres
for linea in fileinput.input(movies):
	idM = ''
	titulo = ''
   	if not fileinput.isfirstline():
		linea = linea.split('"')
		idM, titulo = formatearTitulo(linea)

		if idM in dicmovies:
			dicmovies[idM].append(titulo)
		else:
			dicmovies[idM] = titulo


# in: userId,movieId,rating,timestamp
for linea in fileinput.input(ratings):
   	if not fileinput.isfirstline():
		linea = linea.split(',')
		idM = linea[1]
		titulo = dicmovies[idM]
		print(str(idM)+'__'+str(titulo)+'__'+str(linea[2]))
# out: movieId, title, rating