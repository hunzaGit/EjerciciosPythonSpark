#! /usr/bin/python
import sys

def print_lines(lineas):
    for i,linea in enumerate(lineas):
    	if len(linea) > 0:
        	print linea

#contenido_archivo = sys.stdin.read()

#lineas = contenido_archivo.splitlines()
for lineas in sys.stdin:
	print_lines(lineas)



#Develop a distributed version of the grep tool to search words in very large documents. 
#The output should be the numbers of the lines that match a given pattern. 
#You can use as input file the input text used in the word count example described in class (eBook of Moby Dick).