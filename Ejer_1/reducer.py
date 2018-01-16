#!/usr/bin/python

import sys
import json

# Date  closeValue
# 2017-12-29  1046.400024

diccionario = {}
previous = None
sum = 0



def disgregar(anyo, valor):
	if diccionario.has_key(anyo):
    	diccionario.anyo.acum += float(valor)
    	diccionario.anyo.num += 1
    else:
    	diccionario.anyo.acum = float(valor)
    	diccionario.anyo.num = 1


def media():
	for anyo in diccionario:
		diccionario[anyo].media =  anyo.acum / anyo.num


def printResult():
	for anyo in diccionario:
		print anyo + "\t" + diccionario[anyo].media



for line in sys.stdin:
    anyo, valor = line.split()
    disgregar(anyo,valor)
    

media()
printResult()




#!/usr/bin/python

import sys

previous = None
sum = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print str( sum ) + '\t' + previous
        previous = key
        sum = 0
    
    sum = sum + int( value )

print str( sum ) + '\t' + previous