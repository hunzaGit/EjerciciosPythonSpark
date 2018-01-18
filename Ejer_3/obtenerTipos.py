#!/usr/bin/python

import sys
import re


# name,id,nametype,recclass,mass (g),fall,year,reclat,reclong,GeoLocation

# Tres clases distintos

# ['Bulls Run,5163,Valid,Iron?,2250,Fell,01/01/1964 12:00:00 AM,,,']
#  |--------------------------------------------------------------|

# ['Aachen,1,Valid,L5,21,Fell,01/01/1880 12:00:00 AM,50.775000,6.083330,', '(50.775000, 6.083330)', '\n'] - 3 elemento
#  |--------------------------------------------------------------------|  |---------------------|  |--|

# ['Akyumak,433,Valid,', 'Iron, IVA', ',50000,Fell,01/01/1981 12:00:00 AM,39.916670,42.816670,', '(39.916670, 42.816670)', '\n'] - 5 elementos
#  |------------------|  |----------|  |------------------------------------------------------|  |-----------------------| |--|

def formatearFila(line):
	if len(line) <= 3:
		line = line[0].split(',')
		if len(line)>6:
			tipo = line[2]
			clase = line[3]
		else:
			return None, None
			
	else: # if len(line) > 3:
		tipo = line[0].split(',')[2]
		clase = line[1]

	if tipo != '' and clase != '':
		return tipo, clase
	else:
		return None, None




clasesMeteo = []
clasesMeteoValid = []
clasesMeteoRelict = []

for line in sys.stdin:
	words = re.split('"', line)
	tipo, clase = formatearFila(words)
	if tipo != None and clase != None and clase not in clasesMeteo:
		clasesMeteo.append(clase)
		if tipo == 'Valid':
			clasesMeteoValid.append(clase)
		if tipo == 'Relict':
			clasesMeteoRelict.append(clase)
		
clasesMeteo.sort()
clasesMeteoValid.sort()
clasesMeteoRelict.sort()

print '*************  clasesMeteo  *************'
print clasesMeteo
print len(clasesMeteo)
print '*************  *************  *************'
print
print '*************  clasesMeteoValid  *************'
print clasesMeteoValid
print len(clasesMeteoValid)
print '*************  *************  *************'
print
print '*************  clasesMeteoRelict  *************'
print clasesMeteoRelict
print len(clasesMeteoRelict)
print '*************  *************  *************'




