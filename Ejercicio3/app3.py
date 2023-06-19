
from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import json
from urllib.request import urlopen

class app:

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("290x115")
        self.__ventana.title("Conversor de Moneda")
        self.__ventana.config(bg='skyblue')


        #variables de uso
        self.__dolares = StringVar()
        self.__pesos = StringVar()

        #varibale trace
        self.__dolares.trace('w',self.calcular)




        mainframe = Frame(self.__ventana,width=250,height=100)
        mainframe.place(x=10,y=10,relx=0.01,rely=0.01)

        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'



        
        
        self.__dolaresLabel = Label(mainframe,text="dolares")
        self.__dolaresLabel.place(x=165,y=10)

        self.__dolaresEntry = Entry(mainframe,textvariable=self.__dolares,width=8,relief='solid')
        self.__dolaresEntry.place(x=105,y=10)

        


        #Label(mainframe,text="Original name").place(x=25,y=25,anchor=N)

        self.__EsEquivalenteLabel = ttk.Label(mainframe,text='es equivalente a')
        self.__EsEquivalenteLabel.place(x=10,y=40)

        self.__pesosLabel = Label(mainframe,text='pesos',)
        self.__pesosLabel.place(x=165,y=40)

        self.__pesosResultadoLabel = Label(mainframe,textvariable=self.__pesos)
        self.__pesosResultadoLabel.place(x=105,y=40)
        
        
        self.__butonSalir = Button(mainframe,text='Salir',command=self.__ventana.destroy,justify=CENTER,relief='groove',width=10)
        self.__butonSalir.place(x=165,y=65)




        self.__ventana.mainloop()



    def run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
        dolarventa = float(str(self.__resultado[0]['casa']['venta']).replace(",","."))
        return(dolarventa)
    
    def calcular(self,*args):
        try:
            cantidadDolar = float(self.__dolaresEntry.get())
            valordolar = float(self.run())
            self.__pesos.set(valordolar*cantidadDolar)
        except ValueError:
            #messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
            self.__dolares.set('')
            self.__dolaresEntry.focus()      






if __name__ == '__main__':
    miapp = app()
