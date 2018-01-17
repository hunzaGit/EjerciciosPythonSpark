from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('P3_spark')
sc = SparkContext(conf = conf)


tipoMeteoro = sys.argv[1]


# in: ['2008-12-31','151.117126','154.495163','150.327271','152.830978','152.830978','5811000']
def formatear(line):
	return ( (line[0].split('-'))[0],float(line[4]) )
# out: ['2008',152.830978]

	
rdd = sc.textFile("GOOG.csv")
# Date,Open,High,Low,Close,Adj Close,Volume
# 2008-12-31,151.117126,154.495163,150.327271,152.830978,152.830978,5811000

header = rdd.first()
# Date,Open,High,Low,Close,Adj Close,Volume

rdd = rdd.filter(lambda line: line!=header)
# 2008-12-31,151.117126,154.495163,150.327271,152.830978,152.830978,5811000

lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(","))
# [[line],[line],...]  -- Lineas sin comas
# ['2008-12-31','151.117126','154.495163','150.327271','152.830978','152.830978','5811000']

linesFilter = lines.filter(lambda line: line[0] == tipoMeteoro)

linesNum = linesFilter.map(formatear)
# ['2008',152.830978]

linesNumAcum = linesNum.reduceByKey(lambda acum,n: acum+n)
# ['anyo',sumtotal] 

# Calcular el numero de impactos de cada anyo
# ------------------------------
diasAnyo = linesNum.map(lambda tupla: (tupla[0],1))
# ('2008',1) -- Media diaria 

diasAnyo = diasAnyo.reduceByKey(lambda acum,n: acum+n)
# ('2008',numImpact) -- Numero de dias contabilizados del anyo
# ------------------------------

joinRDD = linesNumAcum.join(diasAnyo)
# ('2008', (sumtotal, numImpact)

mediaAnual = joinRDD.map(lambda tupla: (tupla[0], tupla[1][0]/tupla[1][1]))
# ('2008', media)

mediaAnual = mediaAnual.sortByKey()

mediaAnual.saveAsTextFile("outputP3")