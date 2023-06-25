import json
from pathlib import Path

class ObjectEncoder:
    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            
            if class_name == 'ManejadorPeliculas':
                peliculas = d['peliculas']
                manejador = class_()
                
                for i in range(len(peliculas)):
                    dPeliculas = peliculas[i]
                    class_name = dPeliculas.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPeliculas['__atributos__']
                    unaPelicula = class_(**atributos)
                    manejador.agregarPelicula(unaPelicula)
                
                return manejador

    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)

    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
        
        return diccionario