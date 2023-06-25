from classPelicula import Pelicula
from claseVista import AplicacionPelicula
import tkinter as tk
import json
from classObjectEncoder import ObjectEncoder
from ModeloPelicula import ModeloPelicula
from classPelicula import Pelicula
from controladorPelicula import Controlador



def main():
    apiKey = "8336c985c77f5b489f7837f74a964cd7"
    api_Manager = ModeloPelicula(apiKey)
    vista = AplicacionPelicula()
    encoder = ObjectEncoder("generos.json")
    controlador = Controlador(api_Manager, vista, encoder)
    vista.mainloop()

if __name__ == '__main__':
    main()