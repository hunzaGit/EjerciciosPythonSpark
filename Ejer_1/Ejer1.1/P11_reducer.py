#! /usr/bin/python
import sys

dictionary = {}


def add_line(token, entry_number):
    dictionary[token] = int(entry_number)

def lookfor_word(palabra):
	print("Numero de las lineas en las que aparece la palabra "+ palabra + ":")
	for line in dictionary:

		if palabra in line:
   			sys.stdout.write(str(dictionary[line])+"\n")



palabra_buscada = sys.argv[1]

for i,token in enumerate(sys.stdin.readlines()):
    linea = token
    add_line(linea, i)

lookfor_word(palabra_buscada)