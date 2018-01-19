from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import rank, col, desc
from pyspark.sql.dataframe import DataFrame
import string
import sys
import pandas as pd
import os

conf = SparkConf().setMaster('local').setAppName('FurtherAnalysisMovieRating')
sc = SparkContext(conf = conf)

datos_ratings = pd.read_csv('ratings.csv')
datos_pelis = pd.read_csv('movies.csv')


if not os.path.exists("output"):
    os.makedirs("output")



print "************************************************************"
print('\n -> Calificacion promedio por cada usuario:\n')

medias_valoraciones_por_usuario = datos_ratings.groupby('userId', as_index=False)['rating'].mean()
#print(medias_valoraciones_por_usuario)
medias_valoraciones_por_usuario.to_csv("output/mediaValoracionesUsuario.csv", index=False)

print "************************************************************"




print "************************************************************"
print('\n -> Calificacion promedio general:\n')

media_todas_valoraciones = datos_ratings['rating'].mean()
print(media_todas_valoraciones)
print "************************************************************"




print "************************************************************"
print('\n -> Calificacion promedio de cada pelicula:\n')

medias_valoraciones_por_peli = datos_ratings.groupby('movieId', as_index=False)['rating'].mean()
medias_valoraciones_por_peli = pd.merge(medias_valoraciones_por_peli, datos_pelis.rename(columns={'movieId1':'movieId'}), on='movieId',  how='left')
medias_valoraciones_por_peliFiltered = medias_valoraciones_por_peli.filter(['movieId', 'title', 'rating'])

#print(medias_valoraciones_por_peli)
medias_valoraciones_por_peliFiltered.to_csv("output/valoreacionMediaPorPelicula.csv", index=False)
print "************************************************************"




print "************************************************************"
print('\n -> Caificacion promedio de cada genero:\n')

medias_valoraciones_por_genero = pd.merge(datos_ratings, datos_pelis.rename(columns={'movieId1':'movieId'}), on='movieId',  how='left')
medias_valoraciones_por_genero = medias_valoraciones_por_genero.groupby('genres', as_index=False)['rating'].mean()

#print(medias_valoraciones_por_genero)
medias_valoraciones_por_genero.to_csv("output/valoreacionMediaPorGenero.csv", index=False)
print "************************************************************"




print "************************************************************"
print('\n -> Mejores 10 peliculas:\n')

top10_pelis = medias_valoraciones_por_peli[(medias_valoraciones_por_peli.rating == 5)].head(10).filter(['movieId', 'rating', 'title'])
#print(top10_pelis)
top10_pelis.to_csv("output/top10Pelis.csv", index=False)
print "************************************************************"




print "************************************************************"
print('\n -> Mejores 10 generos:\n')

top10_generos = medias_valoraciones_por_genero[(medias_valoraciones_por_genero.rating == 5)].head(10)
# print(top10_generos)
top10_generos.to_csv("output/top10Generos.csv", index=False)
print "************************************************************"

