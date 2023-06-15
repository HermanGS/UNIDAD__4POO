



from tkinter import *
from tkinter import ttk,messagebox




class app:



    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.geometry("300x250")
        
        self.__PrecioSINVA = StringVar()

        #TITULO

        bloque1 = ttk.Frame(self.__ventana,padding=" 0 0 0 30")
        bloque1.pack(side=TOP,fill=BOTH) 
        self.__titulo = ttk.Label(bloque1,text="Cálculo de IVA",background="lightSkyBlue2",relief="solid",anchor=CENTER,padding=18)
        self.__titulo.pack(side=TOP,fill=BOTH)
        

        #Bloque2 Precio SIn IVA
        bloque2 = ttk.Frame(self.__ventana,padding="0 0 0 0")
        bloque2.pack(side=TOP,fill=BOTH)

        
        self.__PrecioSIVALabel = ttk.Label(bloque2,text=" Precio sin IVA ",padding= "0 0 0 0")
        self.__PrecioSIVALabel.pack(side=TOP)

        self.__PrecioSIVAEntry = ttk.Entry(bloque2,textvariable=self.__PrecioSIVA)
        self.__PrecioSIVAEntry.pack(side=LEFT,fill=BOTH)


        #Bloque3 RadioButton

        bloque3 = ttk.Frame(self.__ventana,padding="0 0 0 0")
        bloque3.pack(side=TOP,fill=BOTH)


        ttk.Radiobutton(bloque3,text="IVA 21 %").pack(side=TOP)
        ttk.Radiobutton(bloque3,text="IVA 10.5 %").pack(side=TOP)


        bloque4 = ttk.Frame(self.__ventana,padding="0 0 0 0")
        bloque4.pack(side=TOP,fill=BOTH)
        
        
        #Bloque4 Botones
        botonSalir = ttk.Button(bloque4,text="Salir",command=self.__ventana.destroy)
        botonSalir.pack(side=BOTTOM)
        
        botonCalcular = ttk.Button(bloque4,text="Calcular",command=self.calcular)
        botonCalcular.pack(side=BOTTOM)
        
        
        self.__ventana.mainloop()


    def calcular(self):
        messagebox.showinfo(title="ola",message="Calculando")

if __name__ == '__main__':
    print("PRINCIPAL")
    Miapp = app()
