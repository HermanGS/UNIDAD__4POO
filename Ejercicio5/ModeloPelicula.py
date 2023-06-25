from classObjectEncoder import ObjectEncoder
from classPelicula import Pelicula
import json
import requests




class ModeloPelicula:
    def __init__(self, api):       
        self.__api = api
        self.__peliculas = []
    
    def ObtenerPeliculas(self):
        url= f"https://api.themoviedb.org/3/discover/movie?api_key={self.__api}"
        respuesta = requests.get(url)
        datos_pelicula = json.loads(respuesta.content)
        if "results" in datos_pelicula:
            peliculas_data = datos_pelicula["results"]
            self.__peliculas = [Pelicula(pelicula_data) for pelicula_data in peliculas_data]
            return self.__peliculas
    
    def Pelicula_en_Detalle(self, id_pelicula):
        url = f"https://api.themoviedb.org/3/movie/{id_pelicula}?api_key={self.__api}"
        respuesta = requests.get(url)
        return json.loads(respuesta.content)
        