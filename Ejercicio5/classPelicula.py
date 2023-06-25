# título, resumen (overview), lenguaje original, fecha de lanzamiento, géneros.
from datetime import datetime
import json

class Pelicula:
    def __init__(self, moviedata):
        self.id = moviedata["id"]
        self.__titulo = moviedata["title"]
        self.__resumen = moviedata["overview"]
        self.__lenguaje = moviedata["original_language"]
        self.__fecha = moviedata["release_date"]
        self.__generos = moviedata["genre_ids"]
    def getid(self):
        return self.id
    def gettitulo(self):
        return self.__titulo
    
    def getresumen(self):
        return self.__resumen
    
    def getlenguaje(self):
        return self.__lenguaje
    
    def getfecha(self):
        return self.__fecha
    
    def getgenero(self):
        return self.__generos
    
    def toJSON(self):
        d = {
                '__class__': self.__class__.__name__,
                '__atributos__': {
                    'title': self.__titulo,
                    'overview': self.__resumen,
                    'original_language': self.__lenguaje,
                    'release_date': self.__fecha,
                    'genre_ids': self.__generos
            }
        }
        return d