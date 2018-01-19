# Ejercicios Python Spark 

Ejercicios de MapReduce y  Spark en Python para la asignatura [Cloud Computing and Big Data](http://www.fdi.ucm.es/Pub/ImpresoFichaDocente.aspx?Id=1312) del Grado de Ingenieria del Software, se ejecutan en una instancia EC2 con una maquina virtual Ubuntu en AWS. [Enunciado del profesor](UCM_-_CLO_-_Fall_2017_-_HW_-_Parallel_Data_Processing.pdf)

## Entorno

 - **Ubuntu** 16.04.3 LTS 
 - **Python** 2.7.12
 - **Spark** 2.2.0
 - **JDK** 1.8.0_151
 - **Scala** 2.11.8





## Ejercicio 1 - MapReduce Programming


### [1.1 Distributed Grep](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.1)
  Realizar una funcion similar a la de la herramineta grep para buscar palabras en documentos grandes
 - **Input**: Libro de Moby Dick en .txt
 - **Output**: Número de linea en la que aparece la palabra buscada
 
#### Ejecución
```shell
$ ./P11_mapper.py < input.txt | sort | ./P11_reducer.py ${PALABRA_BUSCADA} >> output.txt
```


### [2.2 Count URL Access Frequency](https://github.com/hunzaGit/EjerciciosPythonSpark/tree/master/Ejer_1/Ejer_1.2)
  Contar la frecuencia de cada URL en un log de un servidor web
 - **Input**: Log de apache. Fichero obtenido de [MonitorWare](http://www.monitorware.com/es/logsamples/apache.php)
 - **Output**: Tuplas con la frecuencia y la URL
 
#### Ejecución
```shell
$ ./P12_mapper.py < access_log | sort | ./P11_reducer.py >> output.txt
```



### [1.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/tree/master/Ejer_1/Ejer1.3)
  Calcular el precio de cotización promedio diario al cierre de Alphabet Inc. (GOOG) por año desde 2009 usando el patrón MapReduce
 - **Input**: CSV con los datos de cotización de Google. Obtenidos [Yahoo Finance](https://finance.yahoo.com/quote/GOOG/history?ltr=1)
 - **Output**: Tuplas con el año y el precio promedio
 
#### Ejecución
```shell
$ chmod +x P13_mapper.py P13_reducer.py
$ ./P13_mapper.py < GOOG.csv | sort | ./P13_reducer.py >> output.txt
```





## Ejercicio 2 - Spark Programming

### [2.1 Distributed Grep](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.1)
  Realizar una funcion similar a la de la herramineta grep para buscar palabras en documentos grandes
 - **Input**: Libro de Moby Dick en .txt
 - **Output**: Número de linea en la que aparece la palabra buscada
 
#### Ejecución
```shell
$ spark-submit P21_spark.py ${PALABRA_BUSCADA} 
```
    
### [2.2 Count URL Access Frequency](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.2)
  Contar la frecuencia de cada URL en un log de un servidor web
 - **Input**: Log de apache. Fichero obtenido de [MonitorWare](http://www.monitorware.com/es/logsamples/apache.php)
 - **Output**: Tuplas con la URL y su frecuencia
 
#### Ejecución
```shell
$ spark-submit P22_spark.py 
```

### [2.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.3)
  Calcular el precio de cotización promedio diario al cierre de Alphabet Inc. (GOOG) por año desde 2009
 - **Input**: CSV con los datos de cotización de Google. Obtenidos [Yahoo Finance](https://finance.yahoo.com/quote/GOOG/history?ltr=1)
 - **Output**: Tuplas con el año y el precio promedio
 
#### Ejecución
```shell
$ spark-submit P23_spark.py 
```

### [2.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/tree/master/Ejer_2/Ejer_2.4)
  Mostrar las películas con una calificación promedio en los ragos de 1 a 5
 - **Input**: Un fichero CSV con películas y otro con las calificaciones de usuarios. Obtenidos de [GroupLens](https://grouplens.org/datasets/movielens/)
 - **Output**: Tuplas (en el rango pedido) con el el id de película, título y la calificación promedio
 
#### Ejecución
```shell
$ spark-submit P24_spark.py ${RANGO_DE_CALIFICACION}
```




## [Ejercicio 3 - Meteorite Landing](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_3)
  Calcular la masa promedio por año de un tipo de meteorito especificado como un argumento
 - **Input**: CSV que consiste en 45,717 meteoritos e incluye campos como el tipo de meteorito, la masa y el año. Obtenidos de 
 [NASA's Open Data Portal](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh)
 - **Output**: Lista con el año y la masa media de los meteoritos del tipo especificado

### Parametros posibles: 
  > -t tipoMeteoro ['Valid', 'Relict'] (o --tipo) <br>
  > -c claseMeteoro [una de las clases de meteorio] (o --clase) <br>
  > -lc lista las clases de Meteorito (CUIDADO: lista con 460 elementos) (o --listClase) <br>
 
#### Ejecución Map Reduce

```shell
$ chmod +x P3_mapper.py P3_reducer.py
$ ./P3_mapper.py < Meteorite_Landings.csv [-Param] [valueParam] | sort | ./P3_reducer.py >> output.txt
```

#### Ejecución Spark
```shell
$  spark-submit P3_spark.py [-Param] [valueParam]
```
