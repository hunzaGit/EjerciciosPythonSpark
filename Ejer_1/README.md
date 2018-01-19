Ejercicios de la asignatura de Cloud y Big Data
======================
[Enunciado de lproblemas](https://github.com/calope03/EjerciciosCloud/blob/master/Enunciado.pdf)

Para todos los ejercicios es neesario descargar los archivos que se encuentran en la carpeta de cada ejercicio, tantos los de datos como los scripts.

## [Ejercicio 1.2. Count URL Access Frequency](https://github.com/calope03/EjerciciosCloud/tree/master/Ejercicio1_2) ##

Para ejecutar los script P12_mapper.py y P12_redducer.py

    $ chmod +x P12_mapper.py P12_redducer.py
    $ ./P12_mapper.py access_log | sort | ./P12_redducer.py 

Esto devuelve una lista con la URL seguido de cuantas veces aparece


## [Ejercicio 1.4. Movie Rating Data](https://github.com/calope03/EjerciciosCloud/tree/master/Ejercicio1_4) ##

### Apartado A ###

Para ejecutar los script P14a_mapper.py y P14a_redducer.py

    $ chmod +x P14a_mapper.py P14a_redducer.py
    $ ./P14a_mapper.py movies.csv ratings.csv | sort | ./P14a_redducer.py 

Esto devuelve la media de las valoraciones de las peliculas mostrando Titulo valoracionmedia


### Apartado B ###

Para ejecutar los script P14b_mapper.py y P14b_redducer.py

    $ chmod +x P14b_mapper.py P14b_redducer.py
    $ ./P14b_mapper.py movies.csv ratings.csv | sort | ./P14b_redducer.py X
  
Siendo X la media del rango de peliculas que queremos ver.

Los rangos son:

- Si X=1 [0, 1)
- Si X=2 [1, 2)
- Si X=3 [2, 3)
- Si X=4 [3, 4)
- Si X=5 [4, 5)

Esto devuelve la media de las valoraciones de las peliculas, cuyo rango esta entre los escogidos, mostrando Titulo valoracionmedia
