from tkinter import *
from tkinter import ttk, messagebox


class aplicacion:


    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title("Primera ventana xd")
        mainframe = ttk.Frame(self.__ventana,padding ="3 3 12 12")
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__pulgadas = StringVar()
        self.__centimetros = StringVar()
        self.__pulgadasEntry = ttk.Entry(mainframe,width=7,textvariable=self.__pulgadas)
        self.__pulgadasEntry.grid(column=2,row=1,sticky=(W,E))
        ttk.Label(mainframe,textvariable=self.__centimetros).grid(column=2,row=2,sticky=(W,E))
        ttk.Button(mainframe,text="Calculame",command=self.calcular).grid(column=2,row=3,sticky=W)
        ttk.Button(mainframe,text="Salicion",command=self.__ventana.destroy).grid(column=3,row=3,sticky=W)
        ttk.Label(mainframe,text="Pulgadasas").grid(column=3,row=1,sticky=W)
        ttk.Label(mainframe,text="Equivale a => ").grid(column=1,row=2,sticky=E)
        ttk.Label(mainframe,text="Centimetros").grid(column=3,row=2,sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)
        self.__pulgadasEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            valor=float(self.__pulgadasEntry.get())
            self.__centimetros.set(2.54*valor)
        except ValueError:
            messagebox.showerror(title="Error de Tipo",message='Debe Ingresar un valor que sea un Número')
            self.__pulgadas.set("k")
            self.__pulgadasEntry.focus()
    
    

            