from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster('local').setAppName('P23_spark')
sc = SparkContext(conf = conf)



def calcmedia(line):
	med = (line[1]+line[2]+line[3]+line[4])/4
	return (line[0], med)

# ['2008',152.830978]
def formatear(line):
	return ((line[0].split('-'))[0],float(line[4]))
	
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


linesNum = lines.map(formatear)
# ['2008',152.830978]

linesNumAcum = linesNum.reduceByKey(lambda acum,n: acum+n)
# ['anyo',sumtotal] 

# Calcular el mumero de dias de cada anyo
# ------------------------------
diasAnyo = linesNum.map(lambda tupla: (tupla[0],1))
# ('2008',1) -- Media diaria 

diasAnyo = diasAnyo.reduceByKey(lambda acum,n: acum+n)
# ('2008',numDias) -- Numero de dias contabilizados del anyo
# ------------------------------

joinRDD = linesNumAcum.join(diasAnyo)
# ('2008', (sumtotal, numDias)

mediaAnual = joinRDD.map(lambda tupla: (tupla[0], tupla[1][0]/tupla[1][1]))
# ('2008', media)

mediaAnual = mediaAnual.sortByKey()

mediaAnual.saveAsTextFile("output23")