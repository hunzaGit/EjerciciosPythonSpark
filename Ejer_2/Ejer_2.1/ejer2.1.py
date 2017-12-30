from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('P21_spark')
sc = SparkContext(conf = conf)

palabraGrep = sys.argv[1]
palabraGrep = palabraGrep.lower()

def filtro(tupla):
	res = False
	for pal in tupla[0]:
		if palabraGrep in pal:
			res = True
			break
	return res


rdd = sc.textFile("input.txt")
# The Project Gutenberg EBook of Moby Dick; or The Whale, by Herman Melville

lines = rdd.map(lambda x: x.encode("ascii", "ignore").split())
# [[line],[line],...]  -- Lineas sin espacion

lines = lines.map(lambda line: [x.lower() for x in line])
# [[line],[line],...]  -- todas las palabras en minusculas

tuplas = lines.zipWithIndex()
# [ ([line],0) , ([line],1) , ([line],2)]  -- Tuplas con su indice de linea

resultFilter = tuplas.filter(filtro)
# [ ([line],1) , ([line],12) , ([line],56)]  -- Con las tuplas de las lineas que cumplen el filtro

aggreg = resultFilter.map(lambda tupla: tupla[1])
# [1, 12, 56, ...]  -- Solo los indices de las filas

aggreg.saveAsTextFile("output21")