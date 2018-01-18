#!/usr/bin/python

import sys
import re

# ********************************************************************************
# ******************  Variables y Tipos y clases de meteoritos  ******************
# ********************************************************************************

paramTipoMeteo = None
paramClaseMeteo = None


nameType = ['Valid', 'Relict']
# size: 2 elementos
recclass = ['Acapulcoite', 'Acapulcoite/Lodranite', 'Acapulcoite/lodranite', 'Achondrite-prim', 'Achondrite-ung', 'Angrite', 'Aubrite', 'Aubrite-an', 'Brachinite', 'C', 'C1-ung', 'C1/2-ung', 'C2', 'C2-ung', 'C3-ung', 'C3.0-ung', 'C3/4-ung', 'C4', 'C4-ung', 'C4/5', 'C5/6-ung', 'C6', 'CB', 'CBa', 'CBb', 'CH/CBb', 'CH3', 'CH3 ', 'CI1', 'CK', 'CK3', 'CK3-an', 'CK3.8', 'CK3/4', 'CK4', 'CK4-an', 'CK4/5', 'CK5', 'CK5/6', 'CK6', 'CM', 'CM-an', 'CM1', 'CM1/2', 'CM2', 'CM2-an', 'CO3', 'CO3 ', 'CO3.0', 'CO3.1', 'CO3.2', 'CO3.3', 'CO3.4', 'CO3.5', 'CO3.6', 'CO3.7', 'CO3.8', 'CR', 'CR-an', 'CR1', 'CR2', 'CR2-an', 'CR7', 'CV2', 'CV3', 'CV3-an', 'Chondrite-fusion crust', 'Chondrite-ung', 'Diogenite', 'Diogenite-an', 'Diogenite-olivine', 'Diogenite-pm', 'E', 'E-an', 'E3', 'E3-an', 'E4', 'E5', 'E5-an', 'E6', 'EH', 'EH-imp melt', 'EH3', 'EH3/4-an', 'EH4', 'EH4/5', 'EH5', 'EH6', 'EH6-an', 'EH7', 'EH7-an', 'EL-melt rock', 'EL3', 'EL3/4', 'EL4', 'EL4/5', 'EL5', 'EL6', 'EL6 ', 'EL6/7', 'EL7', 'Enst achon', 'Enst achon-ung', 'Eucrite', 'Eucrite-Mg rich', 'Eucrite-an', 'Eucrite-br', 'Eucrite-cm', 'Eucrite-mmict', 'Eucrite-pmict', 'Eucrite-unbr', 'Fusion crust', 'H', 'H(5?)', 'H(?)4', 'H(L)3', 'H(L)3-an', 'H-an', 'H-imp melt', 'H-melt breccia', 'H-melt rock', 'H-metal', 'H/L3', 'H/L3-4', 'H/L3.5', 'H/L3.6', 'H/L3.7', 'H/L3.9', 'H/L4', 'H/L4-5', 'H/L4/5', 'H/L5', 'H/L6', 'H/L6-melt rock', 'H/L~4', 'H3', 'H3 ', 'H3-4', 'H3-5', 'H3-6', 'H3-an', 'H3.0', 'H3.0-3.4', 'H3.05', 'H3.1', 'H3.10', 'H3.15', 'H3.2', 'H3.2-3.7', 'H3.2-6', 'H3.2-an', 'H3.3', 'H3.4', 'H3.4-5', 'H3.4/3.5', 'H3.5', 'H3.5-4', 'H3.6', 'H3.6-6', 'H3.7', 'H3.7-5', 'H3.7-6', 'H3.7/3.8', 'H3.8', 'H3.8-4', 'H3.8-5', 'H3.8-6', 'H3.8-an', 'H3.8/3.9', 'H3.8/4', 'H3.9', 'H3.9-5', 'H3.9-6', 'H3.9/4', 'H3/4', 'H4', 'H4 ', 'H4(?)', 'H4-5', 'H4-6', 'H4-an', 'H4-melt breccia', 'H4/5', 'H4/6', 'H5', 'H5 ', 'H5-6', 'H5-7', 'H5-an', 'H5-melt breccia', 'H5/6', 'H6', 'H6 ', 'H6-melt breccia', 'H6/7', 'H7', 'H?', 'Howardite', 'Howardite-an', 'H~4', 'H~4/5', 'H~5', 'H~6', 'Impact melt breccia', 'Iron', 'Iron, IAB complex', 'Iron, IAB-MG', 'Iron, IAB-an', 'Iron, IAB-sHH', 'Iron, IAB-sHL', 'Iron, IAB-sHL-an', 'Iron, IAB-sLH', 'Iron, IAB-sLL', 'Iron, IAB-sLM', 'Iron, IAB-ung', 'Iron, IAB?', 'Iron, IC', 'Iron, IC-an', 'Iron, IIAB', 'Iron, IIAB-an', 'Iron, IIC', 'Iron, IID', 'Iron, IID-an', 'Iron, IIE', 'Iron, IIE-an', 'Iron, IIF', 'Iron, IIG', 'Iron, IIIAB', 'Iron, IIIAB-an', 'Iron, IIIAB?', 'Iron, IIIE', 'Iron, IIIE-an', 'Iron, IIIF', 'Iron, IVA', 'Iron, IVA-an', 'Iron, IVB', 'Iron, ungrouped', 'Iron?', 'K', 'K3', 'L', 'L(?)3', 'L(H)3', 'L(LL)3', 'L(LL)3.05', 'L(LL)3.5-3.7', 'L(LL)5', 'L(LL)6', 'L(LL)~4', 'L-imp melt', 'L-melt breccia', 'L-melt rock', 'L-metal', 'L/LL', 'L/LL(?)3', 'L/LL-melt rock', 'L/LL3', 'L/LL3-5', 'L/LL3-6', 'L/LL3.10', 'L/LL3.2', 'L/LL3.4', 'L/LL3.5', 'L/LL3.6/3.7', 'L/LL4', 'L/LL4-6', 'L/LL4/5', 'L/LL5', 'L/LL5-6', 'L/LL5/6', 'L/LL6', 'L/LL6-an', 'L/LL~4', 'L/LL~5', 'L/LL~6', 'L3', 'L3-4', 'L3-5', 'L3-6', 'L3-7', 'L3-melt breccia', 'L3.0', 'L3.0-3.7', 'L3.0-3.9', 'L3.00', 'L3.05', 'L3.1', 'L3.10', 'L3.2', 'L3.2-3.5', 'L3.2-3.6', 'L3.3', 'L3.3-3.5', 'L3.3-3.6', 'L3.3-3.7', 'L3.4', 'L3.4-3.7', 'L3.5', 'L3.5-3.7', 'L3.5-3.8', 'L3.5-3.9', 'L3.5-5', 'L3.6', 'L3.6-4', 'L3.7', 'L3.7-3.9', 'L3.7-4', 'L3.7-6', 'L3.7/3.8', 'L3.8', 'L3.8-5', 'L3.8-6', 'L3.8-an', 'L3.9', 'L3.9-5', 'L3.9-6', 'L3.9/4', 'L3/4', 'L4', 'L4 ', 'L4-5', 'L4-6', 'L4-an', 'L4-melt breccia', 'L4-melt rock', 'L4/5', 'L5', 'L5 ', 'L5-6', 'L5-7', 'L5-melt breccia', 'L5/6', 'L6', 'L6 ', 'L6-melt breccia', 'L6-melt rock', 'L6/7', 'L7', 'LL', 'LL(L)3', 'LL(L)3.1', 'LL-imp melt', 'LL-melt breccia', 'LL-melt rock', 'LL3', 'LL3-4', 'LL3-5', 'LL3-6', 'LL3.0', 'LL3.00', 'LL3.05', 'LL3.1', 'LL3.1-3.5', 'LL3.10', 'LL3.15', 'LL3.2', 'LL3.3', 'LL3.4', 'LL3.5', 'LL3.6', 'LL3.7', 'LL3.7-6', 'LL3.8', 'LL3.8-4', 'LL3.8-6', 'LL3.9', 'LL3.9/4', 'LL3/4', 'LL4', 'LL4-5', 'LL4-6', 'LL4/5', 'LL4/6', 'LL5', 'LL5-6', 'LL5-7', 'LL5/6', 'LL6', 'LL6 ', 'LL6(?)', 'LL6-an', 'LL6-melt breccia', 'LL6/7', 'LL7', 'LL7(?)', 'LL<3.5', 'LL~3', 'LL~4', 'LL~4/5', 'LL~5', 'LL~6', 'Lodranite', 'Lodranite-an', 'Lunar', 'Lunar (anorth)', 'Lunar (bas. breccia)', 'Lunar (bas/anor)', 'Lunar (bas/gab brec)', 'Lunar (basalt)', 'Lunar (feldsp. breccia)', 'Lunar (gabbro)', 'Lunar (norite)', 'L~3', 'L~4', 'L~4-6', 'L~5', 'L~6', 'Martian', 'Martian (OPX)', 'Martian (basaltic breccia)', 'Martian (chassignite)', 'Martian (nakhlite)', 'Martian (shergottite)', 'Mesosiderite', 'Mesosiderite-A', 'Mesosiderite-A1', 'Mesosiderite-A2', 'Mesosiderite-A3', 'Mesosiderite-A3/4', 'Mesosiderite-A4', 'Mesosiderite-B', 'Mesosiderite-B1', 'Mesosiderite-B2', 'Mesosiderite-B4', 'Mesosiderite-C', 'Mesosiderite-C2', 'Mesosiderite-an', 'Mesosiderite?', 'OC', 'OC3', 'Pallasite', 'Pallasite, PES', 'Pallasite, PMG', 'Pallasite, PMG-an', 'Pallasite, ungrouped', 'Pallasite?', 'R', 'R3', 'R3-4', 'R3-5', 'R3-6', 'R3.4', 'R3.5-4', 'R3.5-6', 'R3.6', 'R3.7', 'R3.8', 'R3.8-5', 'R3.8-6', 'R3.9', 'R3/4', 'R4', 'R4/5', 'R5', 'R6', 'Relict H', 'Relict OC', 'Relict iron', 'Stone-uncl', 'Stone-ung', 'Unknown', 'Ureilite', 'Ureilite-an', 'Ureilite-pmict', 'Winonaite', 'recclass']
# size: 466 elementos
recclassValid = ['Acapulcoite', 'Acapulcoite/Lodranite', 'Acapulcoite/lodranite', 'Achondrite-prim', 'Achondrite-ung', 'Angrite', 'Aubrite', 'Aubrite-an', 'Brachinite', 'C', 'C1-ung', 'C1/2-ung', 'C2', 'C2-ung', 'C3-ung', 'C3.0-ung', 'C3/4-ung', 'C4', 'C4-ung', 'C4/5', 'C5/6-ung', 'C6', 'CB', 'CBa', 'CBb', 'CH/CBb', 'CH3', 'CH3 ', 'CI1', 'CK', 'CK3', 'CK3-an', 'CK3.8', 'CK3/4', 'CK4', 'CK4-an', 'CK4/5', 'CK5', 'CK5/6', 'CK6', 'CM', 'CM-an', 'CM1', 'CM1/2', 'CM2', 'CM2-an', 'CO3', 'CO3 ', 'CO3.0', 'CO3.1', 'CO3.2', 'CO3.3', 'CO3.4', 'CO3.5', 'CO3.6', 'CO3.7', 'CO3.8', 'CR', 'CR-an', 'CR1', 'CR2', 'CR2-an', 'CR7', 'CV2', 'CV3', 'CV3-an', 'Chondrite-ung', 'Diogenite', 'Diogenite-an', 'Diogenite-olivine', 'Diogenite-pm', 'E', 'E-an', 'E3', 'E3-an', 'E4', 'E5', 'E5-an', 'E6', 'EH', 'EH-imp melt', 'EH3', 'EH3/4-an', 'EH4', 'EH4/5', 'EH5', 'EH6', 'EH6-an', 'EH7', 'EH7-an', 'EL-melt rock', 'EL3', 'EL3/4', 'EL4', 'EL4/5', 'EL5', 'EL6', 'EL6 ', 'EL6/7', 'EL7', 'Enst achon', 'Enst achon-ung', 'Eucrite', 'Eucrite-Mg rich', 'Eucrite-an', 'Eucrite-br', 'Eucrite-cm', 'Eucrite-mmict', 'Eucrite-pmict', 'Eucrite-unbr', 'H', 'H(5?)', 'H(?)4', 'H(L)3', 'H(L)3-an', 'H-an', 'H-imp melt', 'H-melt breccia', 'H-melt rock', 'H-metal', 'H/L3', 'H/L3-4', 'H/L3.5', 'H/L3.6', 'H/L3.7', 'H/L3.9', 'H/L4', 'H/L4-5', 'H/L4/5', 'H/L5', 'H/L6', 'H/L6-melt rock', 'H/L~4', 'H3', 'H3 ', 'H3-4', 'H3-5', 'H3-6', 'H3-an', 'H3.0', 'H3.0-3.4', 'H3.05', 'H3.1', 'H3.10', 'H3.15', 'H3.2', 'H3.2-3.7', 'H3.2-6', 'H3.2-an', 'H3.3', 'H3.4', 'H3.4-5', 'H3.4/3.5', 'H3.5', 'H3.5-4', 'H3.6', 'H3.6-6', 'H3.7', 'H3.7-5', 'H3.7-6', 'H3.7/3.8', 'H3.8', 'H3.8-4', 'H3.8-5', 'H3.8-6', 'H3.8-an', 'H3.8/3.9', 'H3.8/4', 'H3.9', 'H3.9-5', 'H3.9-6', 'H3.9/4', 'H3/4', 'H4', 'H4 ', 'H4(?)', 'H4-5', 'H4-6', 'H4-an', 'H4-melt breccia', 'H4/5', 'H4/6', 'H5', 'H5 ', 'H5-6', 'H5-7', 'H5-an', 'H5-melt breccia', 'H5/6', 'H6', 'H6 ', 'H6-melt breccia', 'H6/7', 'H7', 'H?', 'Howardite', 'Howardite-an', 'H~4', 'H~4/5', 'H~5', 'H~6', 'Impact melt breccia', 'Iron', 'Iron, IAB complex', 'Iron, IAB-MG', 'Iron, IAB-an', 'Iron, IAB-sHH', 'Iron, IAB-sHL', 'Iron, IAB-sHL-an', 'Iron, IAB-sLH', 'Iron, IAB-sLL', 'Iron, IAB-sLM', 'Iron, IAB-ung', 'Iron, IAB?', 'Iron, IC', 'Iron, IC-an', 'Iron, IIAB', 'Iron, IIAB-an', 'Iron, IIC', 'Iron, IID', 'Iron, IID-an', 'Iron, IIE', 'Iron, IIE-an', 'Iron, IIF', 'Iron, IIG', 'Iron, IIIAB', 'Iron, IIIAB-an', 'Iron, IIIAB?', 'Iron, IIIE', 'Iron, IIIE-an', 'Iron, IIIF', 'Iron, IVA', 'Iron, IVA-an', 'Iron, IVB', 'Iron, ungrouped', 'Iron?', 'K', 'K3', 'L', 'L(?)3', 'L(H)3', 'L(LL)3', 'L(LL)3.05', 'L(LL)3.5-3.7', 'L(LL)5', 'L(LL)6', 'L(LL)~4', 'L-imp melt', 'L-melt breccia', 'L-melt rock', 'L-metal', 'L/LL', 'L/LL(?)3', 'L/LL-melt rock', 'L/LL3', 'L/LL3-5', 'L/LL3-6', 'L/LL3.10', 'L/LL3.2', 'L/LL3.4', 'L/LL3.5', 'L/LL3.6/3.7', 'L/LL4', 'L/LL4-6', 'L/LL4/5', 'L/LL5', 'L/LL5-6', 'L/LL5/6', 'L/LL6', 'L/LL6-an', 'L/LL~4', 'L/LL~5', 'L/LL~6', 'L3', 'L3-4', 'L3-5', 'L3-6', 'L3-7', 'L3-melt breccia', 'L3.0', 'L3.0-3.7', 'L3.0-3.9', 'L3.00', 'L3.05', 'L3.1', 'L3.10', 'L3.2', 'L3.2-3.5', 'L3.2-3.6', 'L3.3', 'L3.3-3.5', 'L3.3-3.6', 'L3.3-3.7', 'L3.4', 'L3.4-3.7', 'L3.5', 'L3.5-3.7', 'L3.5-3.8', 'L3.5-3.9', 'L3.5-5', 'L3.6', 'L3.6-4', 'L3.7', 'L3.7-3.9', 'L3.7-4', 'L3.7-6', 'L3.7/3.8', 'L3.8', 'L3.8-5', 'L3.8-6', 'L3.8-an', 'L3.9', 'L3.9-5', 'L3.9-6', 'L3.9/4', 'L3/4', 'L4', 'L4 ', 'L4-5', 'L4-6', 'L4-an', 'L4-melt breccia', 'L4-melt rock', 'L4/5', 'L5', 'L5 ', 'L5-6', 'L5-7', 'L5-melt breccia', 'L5/6', 'L6', 'L6 ', 'L6-melt breccia', 'L6-melt rock', 'L6/7', 'L7', 'LL', 'LL(L)3', 'LL(L)3.1', 'LL-imp melt', 'LL-melt breccia', 'LL-melt rock', 'LL3', 'LL3-4', 'LL3-5', 'LL3-6', 'LL3.0', 'LL3.00', 'LL3.05', 'LL3.1', 'LL3.1-3.5', 'LL3.10', 'LL3.15', 'LL3.2', 'LL3.3', 'LL3.4', 'LL3.5', 'LL3.6', 'LL3.7', 'LL3.7-6', 'LL3.8', 'LL3.8-4', 'LL3.8-6', 'LL3.9', 'LL3.9/4', 'LL3/4', 'LL4', 'LL4-5', 'LL4-6', 'LL4/5', 'LL4/6', 'LL5', 'LL5-6', 'LL5-7', 'LL5/6', 'LL6', 'LL6 ', 'LL6(?)', 'LL6-an', 'LL6-melt breccia', 'LL6/7', 'LL7', 'LL7(?)', 'LL<3.5', 'LL~3', 'LL~4', 'LL~4/5', 'LL~5', 'LL~6', 'Lodranite', 'Lodranite-an', 'Lunar', 'Lunar (anorth)', 'Lunar (bas. breccia)', 'Lunar (bas/anor)', 'Lunar (bas/gab brec)', 'Lunar (basalt)', 'Lunar (feldsp. breccia)', 'Lunar (gabbro)', 'Lunar (norite)', 'L~3', 'L~4', 'L~4-6', 'L~5', 'L~6', 'Martian', 'Martian (OPX)', 'Martian (basaltic breccia)', 'Martian (chassignite)', 'Martian (nakhlite)', 'Martian (shergottite)', 'Mesosiderite', 'Mesosiderite-A', 'Mesosiderite-A1', 'Mesosiderite-A2', 'Mesosiderite-A3', 'Mesosiderite-A3/4', 'Mesosiderite-A4', 'Mesosiderite-B', 'Mesosiderite-B1', 'Mesosiderite-B2', 'Mesosiderite-B4', 'Mesosiderite-C', 'Mesosiderite-C2', 'Mesosiderite-an', 'Mesosiderite?', 'OC', 'OC3', 'Pallasite', 'Pallasite, PES', 'Pallasite, PMG', 'Pallasite, PMG-an', 'Pallasite, ungrouped', 'Pallasite?', 'R', 'R3', 'R3-4', 'R3-5', 'R3-6', 'R3.4', 'R3.5-4', 'R3.5-6', 'R3.6', 'R3.7', 'R3.8', 'R3.8-5', 'R3.8-6', 'R3.9', 'R3/4', 'R4', 'R4/5', 'R5', 'R6', 'Stone-uncl', 'Stone-ung', 'Unknown', 'Ureilite', 'Ureilite-an', 'Ureilite-pmict', 'Winonaite']
# size: 460 elementos
recclassRelict = ['Chondrite-fusion crust', 'Fusion crust', 'Relict H', 'Relict OC', 'Relict iron'] 
# size: 5 elementos
# ********************************************************************************


# ********************************************************************************
# ****************************  Parseo de parametros  ****************************
# ********************************************************************************

def salir():
	string = """
*****************************************************************
 - Instruduzca un tipo de meteorito como segundo parametro para ver la masa media por anyo:
 		-t tipoMeteoro ['Valid', 'Relict'] (o --tipo)
 		-c claseMeteoro [uan de las clases de meteorio] (o --clase)
*****************************************************************"""
	sys.exit(string)




if len(sys.argv)>=3:
	if sys.argv[1] == '-t' or sys.argv[1] == '--tipo':
		if sys.argv[2] in nameType:
			paramTipoMeteo = sys.argv[2]
		else:
			salir()
	elif sys.argv[1] == '-c' or sys.argv[1] == '--clase':
		if sys.argv[2] in recclass:
			paramClaseMeteo = sys.argv[2]
		else:
			salir()
	else:
		salir()
else:
	salir()
# ********************************************************************************


# ********************************************************************************
# ************************  Funcion de formateo de filas  ************************
# ********************************************************************************
# Tres tipos distintos

# ['Bulls Run,5163,Valid,Iron?,2250,Fell,01/01/1964 12:00:00 AM,,,']
#  |--------------------------------------------------------------|

# ['Aachen,1,Valid,L5,21,Fell,01/01/1880 12:00:00 AM,50.775000,6.083330,', '(50.775000, 6.083330)', '\n'] - 3 elemento
#  |--------------------------------------------------------------------|  |---------------------|  |--|

# ['Akyumak,433,Valid,', 'Iron, IVA', ',50000,Fell,01/01/1981 12:00:00 AM,39.916670,42.816670,', '(39.916670, 42.816670)', '\n'] - 5 elementos
#  |------------------|  |----------|  |------------------------------------------------------|  |-----------------------| |--|

# Yamato 791510,26859,Valid,E5-an,9.77,Found,01/01/1979 12:00:00 AM,-71.500000,35.666670, "(-71.500000, 35.666670)"


def formatearFila(line):
	tipoOClase = ''
	masa = ''
	anyo = ''
	if len(line) <= 3:
		line = line[0].split(',')
		if len(line)>6:
			if paramTipoMeteo != None: # Si se busca por tipo
				tipoOClase = line[2] 
			else:					   # Si se busca por Clase
				tipoOClase = line[3]
			masa = line[4]
			fecha = line[6]
		else:
			return None
	else: # if len(line) > 3:
		if paramTipoMeteo != None: # Si se busca por tipo
			tipoOClase = line[0].split(',')[2] 
		else:					   # Si se busca por Clase
			tipoOClase = line[1] 
		masa = line[2].encode("ascii", "ignore").split(',')[1]
		fecha = line[2].encode("ascii", "ignore").split(',')[3]

	if fecha != '': 
		fecha = re.split(' ', fecha)[0] # ['01/01/1880', '12:00:00', 'AM']
		anyo = re.split('/', fecha)[2] # 1880
	
	try:
		float(masa)
		if tipoOClase != '' and masa != '' and anyo != '' and anyo.isdigit():
			return [tipoOClase, masa, anyo] 
		else:
			return None
	except ValueError:
		return None
# ********************************************************************************


# ********************************************************************************
# *************************  Codigo de la funcion Mapper  ************************
# ********************************************************************************

#   0    1    2        3         4      5           6
#  name,id,nametype,recclass,mass (g),fall,       year,            reclat, reclong,       GeoLocation
# Aachen,1, Valid,    L5,     21,     Fell,01/01/1880 12:00:00 AM,50.775000,6.083330,"(50.775000, 6.083330)"

# Se elimina la cabecera
sys.stdin.next()
num = 0
numTotal = 0
for line in sys.stdin:
	words = re.split('"', line)
	tupla = formatearFila(words)
	if tupla != None:
		numTotal += 1
		if paramTipoMeteo != None and tupla[0] == paramTipoMeteo: # Si se busca por tipo
			print( tupla[2] + "\t" + tupla[1])
			num += 1
		elif paramClaseMeteo != None and tupla[0] == paramClaseMeteo:   # Si se busca por Clase
			print( tupla[2] + "\t" + tupla[1] )
			num += 1
# year  massValue
# 1880  21


