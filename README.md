# Ejercicios Python Spark 
Ejercicios de Spark en Python para la asignatura [Cloud Computing and Big Data](http://www.fdi.ucm.es/Pub/ImpresoFichaDocente.aspx?Id=1312) del Grado de Ingenieria del Software, se ejecutan en una instancia EC2 con una maquina virtual Ubuntu en AWS. [Enunciado del profesor](UCM_-_CLO_-_Fall_2017_-_HW_-_Parallel_Data_Processing.pdf)

## Entorno

 - **Ubuntu** 16.04.3 LTS 
 - **Python** 2.7.12
 - **Spark** 2.2.0
 - **JDK** 1.8.0_151
 - **Scala** 2.11.8



## Ejercicio 1 - MapReduce Programming
### [1.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_1/Ejer_1.3)
  Calcular el precio de cotización promedio diario al cierre de Alphabet Inc. (GOOG) por año desde 2009 usando el patrón MapReduce
 - **Input**: CSV con los datos de cotización de Google. Obtenidos [Yahoo Finance](https://finance.yahoo.com/quote/GOOG/history?ltr=1)
 - **Output**: Tuplas con el año y el precio promedio
 
 #### Ejecución
 	*Dar permisos de ejecucion a los ficheros antes de ejecutar*
  
    $ ./mapper.py < GOOG.csv | sort | ./reducer.py >> output.txt
    


## Ejercicio 2 - Spark Programming
### [2.1 Distributed Grep](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.1)
  Realizar una funcion similar a la de la herramineta grep para buscar palabras en documentos grandes
 - **Input**: Libro de Moby Dick en .txt
 - **Output**: Nuero de linea en la que aparece la palabra buscada
 
 #### Ejecución
 
    $ spark-submit ejer21.py ${PALABRA_BUSCADA} 
    
    
### [2.2 Count URL Access Frequency](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.2)
  Contar la frecuencia de cada URL en un log de un servidor web
 - **Input**: Log de apache. Fichero obtenido de [MonitorWare](http://www.monitorware.com/es/logsamples/apache.php)
 - **Output**: Tuplas con la URL y su frecuencia
 
 #### Ejecución
  
    $ spark-submit ejer22.py 
    

### [2.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/blob/master/Ejer_2/Ejer_2.3)
  Calcular el precio de cotización promedio diario al cierre de Alphabet Inc. (GOOG) por año desde 2009
 - **Input**: CSV con los datos de cotización de Google. Obtenidos [Yahoo Finance](https://finance.yahoo.com/quote/GOOG/history?ltr=1)
 - **Output**: Tuplas con el año y el precio promedio
 
 #### Ejecución
  
    $ spark-submit ejer23.py 
   
### [2.3 Stock Summary](https://github.com/hunzaGit/EjerciciosPythonSpark/tree/master/Ejer_2/Ejer_2.4)
  Mostrar las películas con una calificación promedio en los ragos de 1 a 5
 - **Input**: Un fichero CSV con películas y otro con las calificaciones de usuarios. Obtenidos de [GroupLens](https://grouplens.org/datasets/movielens/)
 - **Output**: Tuplas (en el rango pedido) con el el id de película, título y la calificación promedio
 
 #### Ejecución
  
    $ spark-submit ejer24.py ${RANGO_DE_CALIFICACION}
    
