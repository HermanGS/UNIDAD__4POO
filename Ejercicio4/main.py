from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from functools import partial
from ClaseImaginario import  Imaginario


class Aplicacion:

    
    def __init__(self) -> None:
    
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.geometry('200x180')

        mainframe = Frame(self.__ventana,relief='ridge',background='lightgrey')
        mainframe.grid(column=0,row=0,sticky=(W,E,N,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)
        
        mainframe['borderwidth'] = 2
        


        #variables usables
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        self.__poderPonerOperador = False


        #operatorEntry = Entry(mainframe,textvariable=self.__operador,width=10,justify='center',state='disabled')
        #operatorEntry.grid(column=1,row=1,columnspan=1,sticky=(W,E))
        panelEntry = Entry(mainframe,textvariable=self.__panel,width=20,justify='center',state='disabled')
        panelEntry.grid(column=1,row=1,columnspan=4,sticky=(W,E))


        Button(mainframe,text='7',command=partial(self.PonerNumero,'7'),width=8).grid(column=1,row=2,sticky=W)
        Button(mainframe,text='8',command=partial(self.PonerNumero,'8'),width=8).grid(column=2,row=2,sticky=W)
        Button(mainframe,text='9',command=partial(self.PonerNumero,'9'),width=8).grid(column=3,row=2,sticky=W)
        Button(mainframe,text='4',command=partial(self.PonerNumero,'4'),width=8).grid(column=1,row=3,sticky=W)
        Button(mainframe,text='5',command=partial(self.PonerNumero,'5'),width=8).grid(column=2,row=3,sticky=W)
        Button(mainframe,text='6',command=partial(self.PonerNumero,'6'),width=8).grid(column=3,row=3,sticky=W)
        Button(mainframe,text='1',command=partial(self.PonerNumero,'1'),width=8).grid(column=1,row=4,sticky=W)
        Button(mainframe,text='2',command=partial(self.PonerNumero,'2'),width=8).grid(column=2,row=4,sticky=W)
        Button(mainframe,text='3',command=partial(self.PonerNumero,'3'),width=8).grid(column=3,row=4,sticky=W)
        
        Button(mainframe,text='+',command=partial(self.PonerOperador,'+'),width=8).grid(column=1,row=5,sticky=W)
        Button(mainframe,text='0',command=partial(self.PonerNumero,'0'),width=8).grid(column=2,row=5,sticky=W)
        Button(mainframe,text='-',command=partial(self.PonerOperador,'-'),width=8).grid(column=3,row=5,sticky=W)
        
        Button(mainframe,text='*',command=partial(self.PonerOperador,'*'),width=8).grid(column=1,row=6,sticky=W)
        Button(mainframe,text='i',command=partial(self.PonerNumero,'i'),width=8).grid(column=2,row=6,sticky=W)
        Button(mainframe,text='/',command=partial(self.PonerOperador,'/'),width=8).grid(column=3,row=6,sticky=W)
        
        Button(mainframe,text='C',command=self.BorrarUno,width=8).grid(column=1,row=7,sticky=W)
        Button(mainframe,text='AC',command=self.BorrarTodo,width=8).grid(column=3,row=7,sticky=W)
        Button(mainframe,text='=',command=partial(self.PonerOperador,'='),width=8).grid(column=2,row=7,sticky=W)
        

        #label1test = Label(mainframe,text='hola')   aca contraté putas
        #label1test.grid(column=1,row=2,sticky=S)

        self.__ventana.mainloop()


    def PonerNumeroInsert(self,numero):
        if self.__operadorAux == None:
            pass
            


    def PonerNumero(self,numero):
            #if self.__operadorAux == None:
            print("Entro al poner numero")
            valor = self.__panel.get()
            self.__panel.set(valor+numero)

    def BorrarUno(self):
        operadores = ['+','-','*','/']
        
        panel = self.__panel.get()            
        if len(panel) != 0:
            ultimo = panel[-1]
            
            if ultimo in operadores:
                self.__operador.set('')
                        
            panelSinElUltimo = panel[0:-1]
            self.__panel.set(panelSinElUltimo)        
    
    
    def BorrarTodo(self):
        self.__panel.set('')
        self.__operador.set('')
        self.__poderPonerOperador = True


    
    
    
    def ResolverOperacion(self,operando1,operacion,operando2):
        resultado = 0
        operando1 = int(operando1)
        operando2 = int(operando2)
        
        
        if operacion == '+':   resultado = operando1 + operando2
        elif operacion == '-': resultado = operando1 - operando2
        elif operacion == '*': resultado = operando1 * operando2
        elif operacion == '/': resultado = operando1 / operando2
        self.__panel.set(str(resultado))
        self.__operador.set('')

    def ResolverOperacion2(self,operando1,operacion,operando2):
        panel = self.__panel.get()
        
        resultado = eval(panel)
        


        self.__panel.set(str(resultado))
        self.__operador.set('')

    
    def splitearOperacion(self,operador):
        if operador in self.__panel.get():
            pass
    
    def OperadorIgual(self):
            operador = self.__operador.get()
            try:
                operando = self.__panel.get().split(operador)
                primerOperando = operando[0]
                segundoOperando = operando[1]
                print(operando)
                self.ResolverOperacion(primerOperando,operador,segundoOperando)
            except ValueError:
                messagebox.showerror(title='Sintax Error',message='Error de Sintaxis  ''+'' ''-'' ''*'' ''/''     ')
    
    
    def detectorI(self):
        bandera = False
        if 'i' in self.__panel.get():
            bandera = True
        return bandera

    def ImaginarioOperation(self):
                panel = self.__panel.get().split('i')
                print(len(panel))
                print("parte 1: ",panel[0])
                print("parte 2: ",panel[1])
                print("parte 3: ",panel[2])

                print("Primer elemento de la parte 2 : ",panel[1][0])
                
                real1 =  int(panel[0][0])
                imaginaria1 = int(panel[0][2])
                print("real 1 : ",real1)
                print("imaginaria 1 : ",imaginaria1)
                numeroImaginario1 = Imaginario(real1,imaginaria1)
                print("Soy un numero imaginario1 : ",numeroImaginario1)

                real2 =  int(panel[1][1])
                imaginaria2 = int(panel[1][3])
                print("real 1 : ",real2)
                print("imaginaria 1 : ",imaginaria2)
                numeroImaginario2 = Imaginario(real2,imaginaria2)
                print("Soy un numero imaginario2 : ",numeroImaginario2)
                
                
                numeroImaginario3 = numeroImaginario1 / numeroImaginario2
                print("Soy un numero imaginario 3 = numI1 + numI2 = ",numeroImaginario3)

    
    
    
    def resolver(self,num1,operador,num2):
        resultado = 0
        if operador == '+':   resultado = num1 + num2
        elif operador == '-': resultado = num1 - num2
        elif operador == '*': resultado = num1 * num2
        elif operador == '/': resultado = num1 / num2
        return resultado

    def ConversorImaginario(self,real,Imaginaria):
        real = int(real)
        Imaginaria = int(Imaginaria)
        return Imaginario(real,Imaginaria)
    
    def PonerOperador(self,op):
        operadores = ['+','-','*','/']
        
        if op == '=':
            if self.detectorI():
                panel = self.__panel.get().split('i')
                if len(panel) == 3:
                    primerTermino = panel[0]
                    
                    #print("Primer Termino :",primerTermino)
                    
                    primerImaginario = self.ConversorImaginario(primerTermino[0],primerTermino[2])
                    
                    operador = panel[1][0]
                    
                    segundoTermino = panel[1]
                    

                    segundoImaginario = self.ConversorImaginario(segundoTermino[1],segundoTermino[3])

                    resultado = self.resolver(primerImaginario,operador,segundoImaginario)
                    
                    print(resultado)

                    self.__panel.set(str(resultado))




            else:
                operador = self.__operador.get()
                try:
                    operando = self.__panel.get().split(operador)
                    primerOperando = operando[0]
                    segundoOperando = operando[1]
                    print(operando)
                    self.ResolverOperacion2(primerOperando,operador,segundoOperando)
                except ValueError:
                    messagebox.showerror(title='Sintax Error',message='Error de Sintaxis  ''+'' ''-'' ''*'' ''/''     ')

        else:
            if self.__operador.get() == '':      # si el ultimo operador está vacío
                print("sino hay operadores")
                self.__operador.set(op)
                print(self.__operador.get())
                self.__operadorAux = op
                
                valor = self.__panel.get()
                self.__panel.set(valor+op)
                
            else:                                 # si el ultimo operador no está vacío
                if self.__operador.get() != op:
                    
                    panel = self.__panel.get()
                    ultimo = panel[-1]
                    print("Si hay operadores y ")
                    
                    if ultimo in operadores:   # si no es un numero
                        panelSinElUltimo = panel[0:-1]
                        panelnuevo = panelSinElUltimo + op
                        
                        self.__operador.set(op)
                        self.__panel.set(panelnuevo)

                        
                        print("panel : ",panel)
                        print("panelSinElUltimo : ",panelSinElUltimo)
                        print("panelnuevo : ",panelnuevo)
                        print("ultimo = ",ultimo)
                    
                    if ultimo not in operadores:  # si es un numero
                        valor = self.__panel.get()
                        self.__panel.set(valor+op)
                    
                    
                else:
                    print("no hago nada")
                    valor = self.__panel.get()
                    self.__panel.set(valor+op)
                

        


if __name__ == '__main__':


    Miapp = Aplicacion()
    print("------")