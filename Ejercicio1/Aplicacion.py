from tkinter import *
from tkinter import ttk,messagebox


class Aplicacion:


    def __init__(self):

        self.__ventana = Tk()
        self.__ventana.geometry('500x265')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana,padding=" 3 3 12 12 ")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.__PrecioIPC = StringVar()
        self.__divi = 0
        
        ttk.Label(mainframe,text='Item').grid(column=1,row=1,sticky=(S))
        ttk.Label(mainframe,text='Vestimenta').grid(column=1,row=2,sticky=E)
        ttk.Label(mainframe,text='Alimentos').grid(column=1,row=3,sticky=E)
        ttk.Label(mainframe,text='Educación').grid(column=1,row=4,sticky=E)
        
        ttk.Label(mainframe,text='Cantidad').grid(column=2,row=1,sticky=N)
        ttk.Label(mainframe,text='Precio Año Base').grid(column=3,row=1,sticky=N)
        ttk.Label(mainframe,text='Precio Año Actual').grid(column=4,row=1,sticky=N)

        
        ttk.Label(mainframe,text='IPC % = ').grid(column=1,row=6,sticky=S)
        ttk.Label(mainframe,textvariable=self.__divi).grid(column=2,row=7,sticky=S)
        ttk.Label(mainframe,textvariable=self.__PrecioIPC).grid(column=1,row=7,sticky=S)


        ttk.Label(mainframe,text='comediante').grid(column=6,row=6,sticky=(S,W))

        
        
        self.__cantidadVestimenta= StringVar()
        self.__cantidadAlimentos = StringVar()
        self.__cantidadEducacion = StringVar()
       
        self.__precioABVestimenta= StringVar()
        self.__precioABAlimento=   StringVar()
        self.__precioABEducacion=  StringVar()
       
        self.__precioAAVestimenta= StringVar()
        self.__precioAAAlimento=   StringVar()
        self.__precioAAEducacion = StringVar()




        self.__cantidadVestimentaE = ttk.Entry(mainframe,width=10,textvariable=self.__cantidadVestimenta)
        self.__cantidadVestimentaE.grid(column=2,row=2)

        self.__cantidadAlimentosE = ttk.Entry(mainframe,width=10,textvariable=self.__cantidadAlimentos)
        self.__cantidadAlimentosE.grid(column=2,row=3)
        
        self.__cantidadEducacionE = ttk.Entry(mainframe,width=10,textvariable=self.__cantidadEducacion)
        self.__cantidadEducacionE.grid(column=2,row=4)
        

        self.__precioABVestimentaE = ttk.Entry(mainframe,width=10,textvariable=self.__precioABVestimenta)
        self.__precioABVestimentaE.grid(column=3,row=2)

        self.__precioABAlimentoE = ttk.Entry(mainframe,width=10,textvariable=self.__precioABAlimento)
        self.__precioABAlimentoE.grid(column=3,row=3)
        
        self.__precioABEducacionE = ttk.Entry(mainframe,width=10,textvariable=self.__precioABEducacion)
        self.__precioABEducacionE.grid(column=3,row=4)

        
        self.__precioAAVestimentaE = ttk.Entry(mainframe,width=10,textvariable=self.__precioAAVestimenta)
        self.__precioAAVestimentaE.grid(column=4,row=2)
        
        self.__precioAAAlimentoE = ttk.Entry(mainframe,width=10,textvariable=self.__precioAAAlimento)
        self.__precioAAAlimentoE.grid(column=4,row=3)
        
        self.__precioAAEducacionE = ttk.Entry(mainframe,width=10,textvariable=self.__precioAAEducacion)
        self.__precioAAEducacionE.grid(column=4,row=4)



        ttk.Button(mainframe,text="Calcular IPC",command=self.CalculoIPC).grid(column=2,row=6)
        ttk.Button(mainframe,text="Salir",command=self.__ventana.destroy).grid(column=3,row=6)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=10,pady=10)        



        self.__ventana.mainloop()


    def CalculoPrecioAB(self):
        try:
            
            total = int(self.__cantidadVestimentaE.get()) * float(self.__precioABVestimentaE.get()) + int(self.__cantidadAlimentosE.get()) * float(self.__precioABAlimentoE.get()) + int(self.__cantidadEducacionE.get()) * float(self.__precioABEducacionE.get())
            print("ab : ",type(total))
            return total
        except ValueError:
            messagebox.showerror('Error de Tipo',message='Flaco disculpame no podes meter letras en el lugar de los numeros \n mas vale que aprendas infradotado')

    def CalculoPrecioAA(self):
        try:
            total = int(self.__cantidadVestimentaE.get()) * float(self.__precioAAVestimentaE.get()) + int(self.__cantidadAlimentosE.get()) * float(self.__precioAAAlimentoE.get()) + int(self.__cantidadEducacionE.get()) * float(self.__precioAAEducacionE.get())
            return total
        except ValueError:
            messagebox.showerror('Error de Tipo',message='Flaco disculpame no podes meter letras en el lugar de los numeros \n mas vale que aprendas infradotado')


    def CalculoIPC(self):
        totalAB = self.CalculoPrecioAB()
        totalAA = self.CalculoPrecioAA()
        try:
            divi = totalAA/totalAB
        except TypeError:
            messagebox.showerror('Error de Tipo',message='Flaco disculpame te cuesta')
        self.__divi = divi
        print(self.__divi)
        print(type(divi))
        divi = str(divi)
        
        print(type(divi))
        lista = divi.split('.')
        print("lista[1]",lista[1])
        try:
            partedecimal = float(lista[1])
        except ValueError:
            print("No se logro castear la parte decimal")

        self.__PrecioIPC.set(partedecimal*100)


if __name__ == '__main__':
    miapp = Aplicacion()
    print("goka")