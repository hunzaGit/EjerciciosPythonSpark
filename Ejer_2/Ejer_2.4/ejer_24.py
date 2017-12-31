from pyspark import SparkConf, SparkContext
import sys

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
	if int(sys.argv[1])>=1 and int(sys.argv[1])<=5:
		califTop = int(sys.argv[1])
		califBot = califTop-1
	else:
		salir()
else:
	salir()


conf = SparkConf().setMaster('local').setAppName('P23_spark')
sc = SparkContext(conf = conf)

# ***********************************************************************************
# **************************  PROCESAR MEDIA DE PELICULAS  **************************
# ***********************************************************************************

rddR = sc.textFile("ratings.csv")
# userId,movieId,rating,timestamp
# 1,31,2.5,1260759144

header = rddR.first()
# userId,movieId,rating,timestamp

rddR = rddR.filter(lambda line: line!=header)
# 1,31,2.5,1260759144

lines = rddR.map(lambda x: x.encode("ascii", "ignore").split(","))
# [[line],[line],...]  -- Lineas sin comas
# ['1','31','2.5','1260759144']

linesNum = lines.map(lambda line: (line[1],float(line[2])))
# (movieId, rating)
# ('31',2.5)

linesNumAcum = linesNum.reduceByKey(lambda acum,n: acum+n)
# ['movieId',ratingAcum] 

# Calcular el numero de aparicines de cada movie
# ------------------------------
numMovie = linesNum.map(lambda tupla: (tupla[0],1))
# ('movieId',1)

numMovie = numMovie.reduceByKey(lambda acum,n: acum+n)
# ('movieId',numCount) -- Numero de aparicines de cada pelicula
# ------------------------------

joinRDD = linesNumAcum.join(numMovie)
# ('movieId', (ratingAcum, numCount)

movieMed = joinRDD.map(lambda tupla: (tupla[0], tupla[1][0]/tupla[1][1]))
# ('movieId', mediaRating)



# ***********************************************************************************
# ***************************  PROCESAR TITULO PELICULAS  ***************************
# ***********************************************************************************

# Dos tipos distintos
# ['39,Clueless (1995),Comedy|Romance']
# ['40,' , 'Cry, the Beloved Country (1995)' , ',Drama']
def formatearTitulo(line):
	if len(line) == 1:
		line = line[0].encode("ascii", "ignore").split(',')
	if len(line) >= 1:
		id = line[0].encode("ascii", "ignore").split(',')[0]
	return (id, line[1])

rddM = sc.textFile("movies.csv")
# movieId,title,genres
# 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy

header = rddM.first()
# movieId,title,genres

rddM = rddM.filter(lambda line: line!=header)
# 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy

lines = rddM.map(lambda x: x.encode("ascii", "ignore").split('"'))
# [[line],[line],...]  -- Lineas sin comas
# ['1,','Toy Story (1995)',',Adventure|Animation|Children|Comedy|Fantasy']
		

lines2 = lines.map(formatearTitulo)
# (movieId, movieName)

# **********************************************************************************
# ********************************  COMBINAR DATOS  ********************************
# **********************************************************************************

joinRDD = lines2.join(movieMed)
# ('movieId', (movieName, mediaRating))

filtered = joinRDD.filter(lambda tupla: tupla[1][1]>califBot and tupla[1][1]<=califTop)
# ('movieId', (movieName, mediaRating))

result = filtered.sortByKey()

result = result.map(lambda tupla: (tupla[0], tupla[1][0], tupla[1][1]) )
# ('movieId', movieName, mediaRating)

result.saveAsTextFile("output24_calif-" + str(califTop))


