#!/usr/bin/python

import sys
import re


nameType = ['Valid', 'Relict']
# size: 2 elementos
recclass = ['L5', 'H6', 'EH4', 'Acapulcoite', 'L6', 'LL3-6', 'H5', 'L', 'Diogenite-pm', 'Unknown', 'H4', 'H', '"Iron', 'CR2-an', 'LL5', 'CI1', 'L/LL4', 'Eucrite-mmict', 'CV3', 'Ureilite-an', 'Stone-uncl', 'L3', 'Angrite', 'LL6', 'L4', 'Aubrite', 'CM2', 'OC', 'Mesosiderite-A1', 'LL4', 'C2-ung', 'LL3.8', 'Howardite', 'Eucrite-pmict', 'Diogenite', 'LL3.15', 'LL3.9', 'H/L3.9', 'Iron?', 'Eucrite', 'H4-an', 'L/LL6', 'H/L4', 'H4-5', 'L3.7', 'LL3.4', 'Martian (chassignite)', 'EL6', 'H3.8', 'H3-5', 'H5-6', 'Mesosiderite', 'H5-7', 'L3-6', 'H4-6', 'Ureilite', 'Mesosiderite-A3/4', 'CO3.3', 'H3', 'EH3/4-an', 'L/LL5', 'H3.7', 'CBa', 'H4/5', 'H3/4', 'H?', 'H3-6', 'L3.4', 'L3.7-6', 'EH7-an', 'Iron', 'CR2', 'CO3.2', 'K3', 'L5/6', 'CK4', 'L3.6', 'LL3.2', 'CO3.5', 'Lodranite', 'Mesosiderite-A3', 'L3-4', 'H5/6', '"Pallasite', 'Eucrite-cm', 'Pallasite', 'L5-6', 'CO3.6', 'Martian (nakhlite)', 'LL3.6', 'C3-ung', 'H3-4', 'CO3.4', 'EH3', 'Winonaite', 'LL', 'Eucrite-br', 'R3.8-6', 'L4-6', 'EH5', 'LL3.00', 'H3.4', 'Martian (shergottite)', 'Achondrite-ung', 'LL3.3', 'C', 'H/L3.6', 'LL7', 'Mesosiderite-B2', 'LL4-6', 'CO3.7', 'L/LL6-an', 'H3.9/4', 'L3.8', 'LL5-6', 'LL3.8-6', 'L3.9', 'L4-5', 'L3-5', 'LL4/5', 'L4/5', 'H3.9', 'H3.6-6', 'H3.8-5', 'H3.8/4', 'H3.9-5', 'CH3', 'R3.8-5', 'L3.9/4', 'E4', 'CO3', 'Chondrite-ung', 'H~5', 'H~6', 'L/LL3.10', 'EL5', 'LL3', 'L~6', 'L~3', 'H~4', 'L(LL)3.5-3.7', 'H3.6', 'L3.4-3.7', 'L3.5', 'CM1/2', 'Martian (OPX)', 'Brachinite', 'LL7(?)', 'LL6(?)', 'Eucrite-Mg rich', 'H3.5-4', 'EL3', 'R3.6', 'H3.5', 'CM1', 'L/LL3', 'H7', 'L(?)3', 'L3.2', 'L3.7-3.9', 'Mesosiderite-B1', 'LL3.7', 'CO3.0', 'LL3.5', 'L3.7-4', 'Eucrite-unbr', 'CV3-an', 'Lunar (anorth)', 'L3.3', 'Lunar', 'CK6', 'L3.1', 'CK5', 'H3.3', 'H3.7-6', 'E6', 'H3.0', 'H3.1', 'L3.0', 'L/LL3.4', 'C6', 'LL3.0', 'Lunar (gabbro)', 'R4', 'C4', 'C1-ung', 'H5-an', 'EH4/5', 'R3-6', 'Mesosiderite-B4', 'L6/7', 'Relict H', 'L-imp melt', 'CK3', 'H3-an', 'R3.8', 'L~5', 'Mesosiderite-an', 'Mesosiderite-A2', 'C4-ung', 'Mesosiderite-A', 'R3.5-6', 'H3.9-6', 'Ureilite-pmict', 'LL~6', 'CK4/5', 'EL4', 'Lunar (feldsp. breccia)', 'L3.9-6', 'H-an', 'L/LL3-6', 'L/LL3-5', 'H/L3.5', 'H/L3', 'R3-4', 'CK3-an', 'LL4-5', 'H/L6', 'L3/4', 'H-imp melt', 'CR', 'Chondrite-fusion crust', 'H(L)3-an', 'L(LL)3', 'H(L)3', 'R3', 'L7', 'CM-an', 'L/LL~6', 'L/LL~5', 'L~4', 'L/LL~4', 'LL(L)3', 'H3.2', 'L-melt breccia', 'H6-melt breccia', 'H5-melt breccia', 'H-melt rock', 'Eucrite-an', 'Lunar (bas/anor)', 'LL5/6', 'LL3/4', 'H3.4/3.5', 'Lunar (basalt)', 'H/L5', 'H(5?)', 'LL-imp melt', 'Mesosiderite?', 'H~4/5', 'L6-melt breccia', 'L3.5-3.7', 'L3.3-3.7', 'L3.2-3.6', 'L3.3-3.6', 'Acapulcoite/Lodranite', 'Mesosiderite-B', 'CK5/6', 'L3.05', 'C2', 'C4/5', 'L/LL3.2', 'L3.5-5', 'L/LL(?)3', 'H4(?)', 'Relict iron', 'EL4/5', 'L5-7', 'Diogenite-an', 'CR1', 'H5 ', 'L5 ', 'H4 ', 'L4 ', 'E', 'L6 ', 'H3 ', 'LL6 ', 'H-metal', 'H6 ', 'L-metal', 'Relict OC', 'EH', 'Mesosiderite-A4', 'L/LL5/6', 'H3.8-4', 'CBb', 'EL6/7', 'EL7', 'CH/CBb', 'CO3.8', 'H/L~4', 'Mesosiderite-C2', 'R5', 'H4/6', 'L-melt rock', 'H3.7-5', 'LL3.7-6', 'H3.7/3.8', 'L3.7/3.8', 'EH-imp melt', 'R', 'Fusion crust', 'Aubrite-an', 'R6', 'LL-melt rock', 'L3.5-3.9', 'L3.2-3.5', 'L3.3-3.5', 'L3.0-3.7', 'E3-an', 'K', 'E3', 'Acapulcoite/lodranite', 'CK4-an', 'L(LL)3.05', 'L3.10', 'CB', 'Diogenite-olivine', 'EL-melt rock', 'EH6', 'L/LL4/5', 'L3.8-an', 'C5/6-ung', 'CV2', 'Lunar (bas. breccia)', 'L3.8-6', 'R3/4', 'R3.9', 'CK', 'LL3.10', 'R4/5', 'L3.8-5', 'Mesosiderite-C', 'Enst achon', 'H/L3-4', 'L(H)3', 'LL3.1', 'OC3', 'LL6/7', 'R3.7', 'CO3 ', 'CH3 ', 'LL~4', 'LL~4/5', 'L(LL)~4', 'H3.05', 'H3.10', 'Impact melt breccia', 'LL3-5', 'H/L3.7', 'Martian', 'CO3.1', 'Lunar (bas/gab brec)', 'Achondrite-prim', 'LL3-4', 'LL<3.5', 'CK3/4', 'CK3.8', 'L/LL-melt rock', 'H6/7', 'EL6 ', 'CM2-an', 'R3-5', 'L4-melt rock', 'L6-melt rock', 'H/L4/5', 'EL3/4', 'H/L6-melt rock', 'Enst achon-ung', 'L3-7', 'R3.4', 'LL3.05', 'LL4/6', 'LL3.8-4', 'H3.15', 'C3.0-ung', 'LL-melt breccia', 'LL6-melt breccia', 'L5-melt breccia', 'LL(L)3.1', 'LL6-an', 'L4-melt breccia', 'Howardite-an', 'H4-melt breccia', 'Martian (basaltic breccia)', 'L3-melt breccia', 'L~4-6', 'LL~5', 'R3.5-4', 'CR7', 'H-melt breccia', 'Lunar (norite)', 'L3.00', 'H3.0-3.4', 'L/LL4-6', 'CM', 'EH7', 'L4-an', 'E-an', 'H3.8/3.9', 'L3.9-5', 'H3.8-6', 'H3.4-5', 'L3.0-3.9', 'L3.5-3.8', 'H3.2-3.7', 'L3.6-4', 'C3/4-ung', 'L/LL3.5', 'L/LL3.6/3.7', 'H/L4-5', 'LL~3', 'Pallasite?', 'LL5-7', 'LL3.9/4', 'H3.8-an', 'CR-an', 'L/LL5-6', 'L(LL)5', 'L(LL)6', 'LL3.1-3.5', 'E5', 'Lodranite-an', 'H3.2-6', 'H(?)4', 'E5-an', 'H3.2-an', 'EH6-an', 'Stone-ung', 'C1/2-ung', 'L/LL']
# size: 432 elementos
recclassValid = ['"Iron', '"Pallasite', 'Acapulcoite', 'Acapulcoite/Lodranite', 'Acapulcoite/lodranite', 'Achondrite-prim', 'Achondrite-ung', 'Angrite', 'Aubrite', 'Aubrite-an', 'Brachinite', 'C', 'C1-ung', 'C1/2-ung', 'C2', 'C2-ung', 'C3-ung', 'C3.0-ung', 'C3/4-ung', 'C4', 'C4-ung', 'C4/5', 'C5/6-ung', 'C6', 'CB', 'CBa', 'CBb', 'CH/CBb', 'CH3', 'CH3 ', 'CI1', 'CK', 'CK3', 'CK3-an', 'CK3.8', 'CK3/4', 'CK4', 'CK4-an', 'CK4/5', 'CK5', 'CK5/6', 'CK6', 'CM', 'CM-an', 'CM1', 'CM1/2', 'CM2', 'CM2-an', 'CO3', 'CO3 ', 'CO3.0', 'CO3.1', 'CO3.2', 'CO3.3', 'CO3.4', 'CO3.5', 'CO3.6', 'CO3.7', 'CO3.8', 'CR', 'CR-an', 'CR1', 'CR2', 'CR2-an', 'CR7', 'CV2', 'CV3', 'CV3-an', 'Chondrite-ung', 'Diogenite', 'Diogenite-an', 'Diogenite-olivine', 'Diogenite-pm', 'E', 'E-an', 'E3', 'E3-an', 'E4', 'E5', 'E5-an', 'E6', 'EH', 'EH-imp melt', 'EH3', 'EH3/4-an', 'EH4', 'EH4/5', 'EH5', 'EH6', 'EH6-an', 'EH7', 'EH7-an', 'EL-melt rock', 'EL3', 'EL3/4', 'EL4', 'EL4/5', 'EL5', 'EL6', 'EL6 ', 'EL6/7', 'EL7', 'Enst achon', 'Enst achon-ung', 'Eucrite', 'Eucrite-Mg rich', 'Eucrite-an', 'Eucrite-br', 'Eucrite-cm', 'Eucrite-mmict', 'Eucrite-pmict', 'Eucrite-unbr', 'H', 'H(5?)', 'H(?)4', 'H(L)3', 'H(L)3-an', 'H-an', 'H-imp melt', 'H-melt breccia', 'H-melt rock', 'H-metal', 'H/L3', 'H/L3-4', 'H/L3.5', 'H/L3.6', 'H/L3.7', 'H/L3.9', 'H/L4', 'H/L4-5', 'H/L4/5', 'H/L5', 'H/L6', 'H/L6-melt rock', 'H/L~4', 'H3', 'H3 ', 'H3-4', 'H3-5', 'H3-6', 'H3-an', 'H3.0', 'H3.0-3.4', 'H3.05', 'H3.1', 'H3.10', 'H3.15', 'H3.2', 'H3.2-3.7', 'H3.2-6', 'H3.2-an', 'H3.3', 'H3.4', 'H3.4-5', 'H3.4/3.5', 'H3.5', 'H3.5-4', 'H3.6', 'H3.6-6', 'H3.7', 'H3.7-5', 'H3.7-6', 'H3.7/3.8', 'H3.8', 'H3.8-4', 'H3.8-5', 'H3.8-6', 'H3.8-an', 'H3.8/3.9', 'H3.8/4', 'H3.9', 'H3.9-5', 'H3.9-6', 'H3.9/4', 'H3/4', 'H4', 'H4 ', 'H4(?)', 'H4-5', 'H4-6', 'H4-an', 'H4-melt breccia', 'H4/5', 'H4/6', 'H5', 'H5 ', 'H5-6', 'H5-7', 'H5-an', 'H5-melt breccia', 'H5/6', 'H6', 'H6 ', 'H6-melt breccia', 'H6/7', 'H7', 'H?', 'Howardite', 'Howardite-an', 'H~4', 'H~4/5', 'H~5', 'H~6', 'Impact melt breccia', 'Iron', 'Iron?', 'K', 'K3', 'L', 'L(?)3', 'L(H)3', 'L(LL)3', 'L(LL)3.05', 'L(LL)3.5-3.7', 'L(LL)5', 'L(LL)6', 'L(LL)~4', 'L-imp melt', 'L-melt breccia', 'L-melt rock', 'L-metal', 'L/LL', 'L/LL(?)3', 'L/LL-melt rock', 'L/LL3', 'L/LL3-5', 'L/LL3-6', 'L/LL3.10', 'L/LL3.2', 'L/LL3.4', 'L/LL3.5', 'L/LL3.6/3.7', 'L/LL4', 'L/LL4-6', 'L/LL4/5', 'L/LL5', 'L/LL5-6', 'L/LL5/6', 'L/LL6', 'L/LL6-an', 'L/LL~4', 'L/LL~5', 'L/LL~6', 'L3', 'L3-4', 'L3-5', 'L3-6', 'L3-7', 'L3-melt breccia', 'L3.0', 'L3.0-3.7', 'L3.0-3.9', 'L3.00', 'L3.05', 'L3.1', 'L3.10', 'L3.2', 'L3.2-3.5', 'L3.2-3.6', 'L3.3', 'L3.3-3.5', 'L3.3-3.6', 'L3.3-3.7', 'L3.4', 'L3.4-3.7', 'L3.5', 'L3.5-3.7', 'L3.5-3.8', 'L3.5-3.9', 'L3.5-5', 'L3.6', 'L3.6-4', 'L3.7', 'L3.7-3.9', 'L3.7-4', 'L3.7-6', 'L3.7/3.8', 'L3.8', 'L3.8-5', 'L3.8-6', 'L3.8-an', 'L3.9', 'L3.9-5', 'L3.9-6', 'L3.9/4', 'L3/4', 'L4', 'L4 ', 'L4-5', 'L4-6', 'L4-an', 'L4-melt breccia', 'L4-melt rock', 'L4/5', 'L5', 'L5 ', 'L5-6', 'L5-7', 'L5-melt breccia', 'L5/6', 'L6', 'L6 ', 'L6-melt breccia', 'L6-melt rock', 'L6/7', 'L7', 'LL', 'LL(L)3', 'LL(L)3.1', 'LL-imp melt', 'LL-melt breccia', 'LL-melt rock', 'LL3', 'LL3-4', 'LL3-5', 'LL3-6', 'LL3.0', 'LL3.00', 'LL3.05', 'LL3.1', 'LL3.1-3.5', 'LL3.10', 'LL3.15', 'LL3.2', 'LL3.3', 'LL3.4', 'LL3.5', 'LL3.6', 'LL3.7', 'LL3.7-6', 'LL3.8', 'LL3.8-4', 'LL3.8-6', 'LL3.9', 'LL3.9/4', 'LL3/4', 'LL4', 'LL4-5', 'LL4-6', 'LL4/5', 'LL4/6', 'LL5', 'LL5-6', 'LL5-7', 'LL5/6', 'LL6', 'LL6 ', 'LL6(?)', 'LL6-an', 'LL6-melt breccia', 'LL6/7', 'LL7', 'LL7(?)', 'LL<3.5', 'LL~3', 'LL~4', 'LL~4/5', 'LL~5', 'LL~6', 'Lodranite', 'Lodranite-an', 'Lunar', 'Lunar (anorth)', 'Lunar (bas. breccia)', 'Lunar (bas/anor)', 'Lunar (bas/gab brec)', 'Lunar (basalt)', 'Lunar (feldsp. breccia)', 'Lunar (gabbro)', 'Lunar (norite)', 'L~3', 'L~4', 'L~4-6', 'L~5', 'L~6', 'Martian', 'Martian (OPX)', 'Martian (basaltic breccia)', 'Martian (chassignite)', 'Martian (nakhlite)', 'Martian (shergottite)', 'Mesosiderite', 'Mesosiderite-A', 'Mesosiderite-A1', 'Mesosiderite-A2', 'Mesosiderite-A3', 'Mesosiderite-A3/4', 'Mesosiderite-A4', 'Mesosiderite-B', 'Mesosiderite-B1', 'Mesosiderite-B2', 'Mesosiderite-B4', 'Mesosiderite-C', 'Mesosiderite-C2', 'Mesosiderite-an', 'Mesosiderite?', 'OC', 'OC3', 'Pallasite', 'Pallasite?', 'R', 'R3', 'R3-4', 'R3-5', 'R3-6', 'R3.4', 'R3.5-4', 'R3.5-6', 'R3.6', 'R3.7', 'R3.8', 'R3.8-5', 'R3.8-6', 'R3.9', 'R3/4', 'R4', 'R4/5', 'R5', 'R6', 'Stone-uncl', 'Stone-ung', 'Unknown', 'Ureilite', 'Ureilite-an', 'Ureilite-pmict', 'Winonaite']
# size: 427
recclassRelict = ['Chondrite-fusion crust', 'Fusion crust', 'Relict H', 'Relict OC', 'Relict iron'] 
# size: 5


def salir():
	string = """
*****************************************************************
 - Instruduzca un tipo de meteorito como segundo parametro para ver la masa media por anyo:
 		-- Consultar los tipos de meteorito --
 		- 'Valid' 
 		- 'Relict'
*****************************************************************"""
	sys.exit(string)
	

if len(sys.argv)>1:
	if sys.argv[1] in nameType:
		paramTipoMeteo = sys.argv[1]
	else:
		salir()
else:
	salir()


# Tres tipos distintos

# ['Bulls Run,5163,Valid,Iron?,2250,Fell,01/01/1964 12:00:00 AM,,,']
#  |--------------------------------------------------------------|

# ['Aachen,1,Valid,L5,21,Fell,01/01/1880 12:00:00 AM,50.775000,6.083330,', '(50.775000, 6.083330)', '\n'] - 3 elemento
#  |--------------------------------------------------------------------|  |---------------------|  |--|

# ['Akyumak,433,Valid,', 'Iron, IVA', ',50000,Fell,01/01/1981 12:00:00 AM,39.916670,42.816670,', '(39.916670, 42.816670)', '\n'] - 5 elementos
#  |------------------|  |----------|  |------------------------------------------------------|  |-----------------------| |--|

def formatearFila(line):
	tipo = ''
	masa = ''
	anyo = ''
	if len(line) <= 3:
		line = line[0].split(',')
		if len(line)>6:
			tipo = line[2]
			masa = line[4]
			fecha = line[6]
		else:
			return None
			
	else: # if len(line) > 3:
		tipo = line[0].split(',')[2]
		masa = line[2].encode("ascii", "ignore").split(',')[1]
		fecha = line[2].encode("ascii", "ignore").split(',')[3]

	if fecha != '': 
		fecha = re.split(' ', fecha)[0] # ['01/01/1880', '12:00:00', 'AM']
		anyo = re.split('/', fecha)[2] # 1880

	if tipo != '' and masa != '' and masa.isdigit() and anyo != '' and anyo.isdigit():
		return [tipo, masa, anyo] 
	else:
		return None
	


#   0    1    2        3         4      5           6
#  name,id,nametype,recclass,mass (g),fall,       year,            reclat, reclong,       GeoLocation
# Aachen,1, Valid,    L5,     21,     Fell,01/01/1880 12:00:00 AM,50.775000,6.083330,"(50.775000, 6.083330)"

# Se elimina la cabecera
sys.stdin.next()

for line in sys.stdin:
	words = re.split('"', line)
	tupla = formatearFila(words)
	if tupla != None and tupla[0] == paramTipoMeteo:
		print( tupla[2] + "\t" + tupla[1] )
# year  massValue
# 1880  21
