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

# Indicamos la ruta donde nltk buscara los datos descargados en nuestro computador.
nltk.data.path.append (r'C:\Users\Jazz\AppData\Roaming\nltk_data')
nltk.download('punkt') # Es un paquete para dividir frases en palabras
nltk.download('wordnet') # Paquete para encontrar sinónimos en palabras

# Función para cargar las películas desde un archivo csv

def load_movies():
    # Leemos el archivo que contiene información de peliculas y seleccionamos las columnas más importantes
    df = pd.read_csv(r"./Dataset/netflix_titles.csv")[['show_id','title','release_year','listed_in','rating','description']]
    
# Renombramos las columnas para que sean más fáciles de entender
    df.columns = ['id','title','year','category','rating','overview']
    
# Llenamos los espacios vacíos con texto vacío y convertimos los datos en una lista de diccionarios
    return df.fillna('').to_dict(orient='records')

# Cargamos las películas al inicial la API para no leer el archivo cada vez que alguien pregunte por ellas
movies_list = load_movies()

# Función para encontrar sinonimos de una palabra
def get_synonyms(word): 
    # Usamos wordnet para encontrar distintas palabras que significan lo mismo
    return{lemma.name().lower() for syn in wordnet.synset(word) for lemma in syn.lemmas()}

# Creamos la aplicación FastAPI, que será el motor de nuestra API
# Esto inicializa la API con un nombre y una versión
app = FastAPI(tittle='Mi aplicacion de peliculas', version='1.0.0')

@app.get('/', tags=['Home'])
def home():
    # cuando entremos al navegador a http://127.0.0.1:8000/ veremos un mensaje de bienvenida
    return HTMLResponse('<h1>Bienvenido a la API de peliculas </h1>')
