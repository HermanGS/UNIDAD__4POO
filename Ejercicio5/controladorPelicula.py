from classPelicula import Pelicula
from claseVista import AplicacionPelicula
import tkinter as tk
import json
class Controlador:
    def __init__(self, api, view, encoder):
        self.__api = api
        self.__view = view
        self.__encoder = encoder
        
        self.__view.SeleccionarPelicula(self.MostrarDatosPeli)
        
        self.peli = self.__api.ObtenerPeliculas()
        self.guardarEnArchivo()
        self.__view.actualizar_lista(self.peli)
    
    def guardarEnArchivo(self):
        peliculas_data = [pelicula.toJSON() for pelicula in self.peli]
        self.__encoder.guardarJSONArchivo(peliculas_data)
        
    def MostrarDatosPeli(self, id):
        index = self.__view.listBox.curselection()[0]
        pelicula = self.peli[index]
        pelicula_detalle = self.__api.Pelicula_en_Detalle(pelicula.id)

        details_window = tk.Toplevel(self.__view)
        details_window.title(pelicula.gettitulo())
        salir = tk.Button(details_window, text="Salir", command=details_window.destroy)
        salir.pack(pady=10, side=tk.BOTTOM)

        title_label = tk.Label(details_window, font="bold 10", bg="sky blue", text="Título: " + pelicula_detalle["title"])
        title_label.pack(pady=10)


        overview_text = tk.Text(details_window, font="bold 10", bg="sky blue", width=40, height=10)
        overview_text.pack(padx=10, pady=10, expand=True)



        resumen = "Resumen: " + pelicula_detalle["overview"]
        overview_text.insert(tk.END, resumen)

        language_label = tk.Label(details_window, font="bold 10", bg="sky blue", text="Lenguaje original: " + pelicula_detalle["original_language"])
        language_label.pack(pady=10, padx=10)

        release_date_label = tk.Label(details_window, font="bold 10", bg="sky blue", text="Fecha de lanzamiento: " + pelicula_detalle["release_date"])
        release_date_label.pack(pady=10, padx=10)

        genres_label = tk.Label(details_window, font="bold 10", bg="sky blue", text="Géneros: " + ", ".join([genre["name"] for genre in pelicula_detalle["genres"]]))
        genres_label.pack(pady=10, padx=10)
