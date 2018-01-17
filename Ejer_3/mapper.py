#!/usr/bin/python

import sys
import re


def salir():
	string = """
*****************************************************************
 - Instruduzca una calificacion del 1 al 5 para ver el listado de peliculas:
	(1) 1 o inferior
	(2) 2 o inferior (pero mayor que 1) 
	(3) 3 o menos (pero mas de 2)
	(4) 4 o menos (pero mas de 3)
	(5) 5 o menos (pero mas de 4)
*****************************************************************"""
	sys.exit(string)
	

if len(sys.argv)>1:
	if int(sys.argv[1])>=1 and int(sys.argv[1])<=5: # if sys.argv[1] in arrayTiposMeteorito
		tipoMeteo = sys.argv[1]
	else:
		salir()
else:
	salir()



# Meteorito,masa,anyo
# id001,  2222, 2017-02-01

tipoMeteo = sys.argv[1]

for line in sys.stdin:
	words = re.split(',', line)
	if words[0] == tipoMeteo:
		anyo = re.split('-', words[3])[0]
		print( anyo + "\t" + words[1] )