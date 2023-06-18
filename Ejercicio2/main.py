"""Ejercicio 2
Una empresa de venta de grandes equipos de aire acondicionado, necesita desarrollar una aplicación que le permita el cálculo del IVA (Impuesto al Valor Agregado), sobre el precio base (sin IVA), de cada uno de los aires acondicionados que vende. 

Regla de negocio: el cálculo del IVA se calcula de la siguiente forma:

 Precio Base*10.5/100 para los artículos grabados con el 10.5%
 Precio Base * 21/100 para los artículos grabados con el 21%
El analista funcional de la empresa ha diseñado una interface para llevar a cabo la tarea solicitada, la que se le provee a usted para el desarrollo de la aplicación."""


from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk



class app:



    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.geometry("335x340")
        self.__ventana.resizable(False, False)
        
        self.__PrecioSinIVA = StringVar()
        self.__booleanoaIVA = BooleanVar()

        self.__IVAvariable = StringVar()
        
        self.__PrecioConIVA = StringVar()



        #TITULO

        bloque1 = ttk.Frame(self.__ventana,padding=" 0 0 0 40")
        bloque1.pack(side=TOP,fill=BOTH) 
        self.__titulo = ttk.Label(bloque1,text="Cálculo de IVA",background="lightSkyBlue2",relief="solid",anchor=CENTER,padding=15)
        self.__titulo.pack(side=TOP,fill=BOTH)
        

        #Bloque2 Precio SIn IVA
        bloque2 = ttk.Frame(self.__ventana,padding="0 0 0 20")
        bloque2.pack(side=TOP,fill=BOTH)
        
                                                                                    #L  N D S
        self.__PrecioSIVALabel = ttk.Label(bloque2,text=" Precio sin IVA ",padding= "20 5 60 5")
        self.__PrecioSIVALabel.pack(side=LEFT)

        self.__PrecioSIVAEntry = ttk.Entry(bloque2,textvariable=self.__PrecioSinIVA,width=20,justify=CENTER)
        self.__PrecioSIVAEntry.pack(side=LEFT,fill=BOTH)
        self.__PrecioSIVAEntry.focus()

        #bloque2['relief'] = 'sunken' 

        #Bloque3 RadioButton

        bloque3 = ttk.Frame(self.__ventana,padding="0 0 220 15")
        bloque3.pack(side=TOP,fill=BOTH)
        ttk.Radiobutton(bloque3,text="IVA 21 %",padding="0 0 0 10",value=0,variable=self.__booleanoaIVA).pack(side=TOP)
        

        ttk.Radiobutton(bloque3,text="IVA 10.5 %",padding="10 0 0 0",value=1,variable=self.__booleanoaIVA).pack(side=TOP)
        #bloque3['relief'] = 'sunken' 
        #-------------------------------------------------------------------------------------
        #Bloque 4 Labels Results

        bloque4 = ttk.Frame(self.__ventana,padding="90 10 0 10")
        bloque4.pack(side=TOP,fill=BOTH)
        #bloque4['relief'] = 'sunken'

        self.__IvaLabel = ttk.Label(bloque4,text="IVA",justify=CENTER)
        self.__IvaLabel.pack(side=LEFT)

        self.__IvaLabelResult = ttk.Label(bloque4,background="white",textvariable=self.__IVAvariable,relief="solid",padding="50 5 60 5",justify=CENTER)
        self.__IvaLabelResult.pack(side=TOP)


        bloque42 = ttk.Frame(self.__ventana,padding="30 0 0 0")
        bloque42.pack(side=TOP,fill=BOTH)
        #bloque42['relief'] = 'sunken'

        self.__PrecioConIVALabel = ttk.Label(bloque42,text="Precio Con IVA",justify=CENTER,padding="0 0 0 0")
        self.__PrecioConIVALabel.pack(side=LEFT)

        self.__PrecioConIVALabelResult = ttk.Label(bloque42,background="white",textvariable=self.__PrecioConIVA,relief="solid",padding="50 5 60 5",justify=CENTER)
        self.__PrecioConIVALabelResult.pack(side=TOP)


        #Bloque43
        bloque43 = ttk.Frame(self.__ventana,padding="30 0 0 0")
        bloque43.pack(side=RIGHT,fill=BOTH)
        #bloque43['relief'] = 'sunken'
        #self.__IvaLabelResult = ttk.Label(bloque43,background="white",text="",relief="solid",padding="50 5 60 5")
        #self.__IvaLabelResult.pack(side=TOP)
        
        #self.__PrecioConIVALabelResult = ttk.Label(bloque43,background="white",text="",relief="solid",padding="50 5 60 5")
        #self.__PrecioConIVALabelResult.pack(side=TOP)

        #Bloque5 Botones
        bloque5 = ttk.Frame(self.__ventana,padding="40 20 50 10")
        bloque5.pack(side=TOP,fill=BOTH)
        #bloque5['relief'] = 'raised'
        """
        botonCalcular = ttk.Button(bloque5,text="Calcular",command=self.CalculoIVA,padding="0 0 0 0")
        botonCalcular.pack(side=LEFT)

        botonSalir = ttk.Button(bloque5,text="Salir",command=self.__ventana.destroy)
        botonSalir.pack(side=RIGHT)
        
        """
        botonCalcular2 = tk.Button(bloque5,text="Calcular",command=self.CalculoIVA,bg='#d5e8d4',relief='solid',width=11)
        botonCalcular2.pack(side=LEFT,fill=BOTH)

        botonSalir2 = tk.Button(bloque5,text="Salir",command=self.__ventana.destroy,bg='#f8cecc',relief='solid',width=11,padx=3,pady=3)
        botonSalir2.pack(side=RIGHT,fill=BOTH)

        boton3 = tk.Button(bloque5,text="Acerca de",command=self.acercade,bg='lightblue',relief='solid')
        #boton3.pack(side=BOTTOM)
        
        self.__ventana.mainloop()


    def CalculoIVA(self):
        #try:    
            
            
            try:
                valor = float(self.__PrecioSinIVA.get())
                
                if self.__booleanoaIVA.get() == 0:
                    IVA = 21.0

                elif self.__booleanoaIVA.get() == 1:
                    IVA = 10.5
                
                ivacalculo = IVA/100
                self.__IVAvariable.set(ivacalculo)
                self.__PrecioConIVA.set(valor*ivacalculo)

            except ValueError :
                messagebox.showerror(title="Error de tipo",message="ERROR - Solo debe ingresar números")
        #except TypeError:
         #   messagebox.showerror(title="ERROR Vacío",message="ERROR - Se debe ingresar algún número")

        


    def acercade(self):
        
        

        messagebox.showinfo(title="Buenas",message="Creador : Herman Gabriel Soria \nDni : 44808998 \nNúmeroDeRegistro : 21728 \nBuenas noches... y Buenos Días...")
        


if __name__ == '__main__':
    print("PRINCIPAL")
    Miapp = app()