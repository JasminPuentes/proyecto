"""
Imagina que esta API es una biblioteca de peliculas
La función load_movies() es como una biblioteca que carga el catalogo de libros (peliculas) cuando se abre la bibliote.
La función get_movies() muestra todo el catalogo cuando alguien lo pide.
La función get_movie() es como si alguien preguntara por un libro (pelicula) especifico es decir, por un codigo de identificación.
La función chatbot (query) es un asistente que busca peliculas segun palabras clave y sinonimo
La función get_movies_by_category (category) ayuda a encontrar peliculas segun su genero (accion, comedia, etc...)
"""

#Importamos las herramientas necesarias para continuar nuestra API
from fastapi import FastAPI, HTTPException #fastAPI nos ayuda a crear la API y HTTPException nos ayuda a manejar errores
from fastapi.responses import HTMLResponse, JSONResponse #HTMLResponse nos ayuda a manejar respuestas HTML y JSONResponse nos ayuda a manejar respuestas JSON
import pandas as pd #pandas nos ayuda a manejr datos en tablas como si fuera un excel
import nltk #nltk es una libreria para procesar texto y analizar palabras
from nltk.tokenize import word_tokenize #word_tokenize nos ayuda a tokenizar texto, es decir, a convertirlo en palabras
from nltk.corpus import wordnet #wordnet es una base de datos de sinonimos de una palabra

#Indicamos la ruta donde nltk buscara los datos descargados en nuestro computador
nltk.data.path.append (':\Users\Jazz\AppData\Roaming\nltk_data')
nltk.download('punkt')
