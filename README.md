# Ejercicios Python Spark 
Ejercicios de Spark en Python para la asignatura [Cloud Computing and Big Data](http://www.fdi.ucm.es/Pub/ImpresoFichaDocente.aspx?Id=1312) del Grado de Ingenieria del Software, se ejecutan en una instancia EC2 con una maquina virtual Ubuntu en AWS. [Enunciado del profesor]()

## Ejercicio 2
### 2.1 Distributed Grep
  Realizar una funcion similar a la de la herramineta grep para buscar palabras en documentos grandes
 - **Input**: Libro de Moby Dick en .txt
 - **Output**: Nuero de linea en la que aparece la palabra buscada
 
 #### Ejecución
 
    $ spark-submit ejer21.py ${PALABRA_BUSCADA} 
    
    
### 2.2 Count URL Access Frequency
  Contar la frecuencia de cada URL en un log de un servidor web
 - **Input**: Log de apache. Fichero obtenido de esta [web](http://www.monitorware.com/es/logsamples/apache.php)
 - **Output**: Tuplas con la URL y su frecuencia
 
 #### Ejecución
  
    $ spark-submit ejer22.py 
    

### 2.3 Stock Summary
  Calcular el precio de cotización promedio diario al cierre de Alphabet Inc. (GOOG)por año desde 2009
 - **Input**: CSV con los datos de cotización de Google. Obtenidos [aquí](https://finance.yahoo.com/quote/GOOG/history?ltr=1)
 - **Output**: Tuplas con el año y el precio promedio
 
 #### Ejecución
  
    $ spark-submit ejer23.py 
