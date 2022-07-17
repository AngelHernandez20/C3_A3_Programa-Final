from tkinter import END

#from openpyxl import Workbook
from Tabla import tablaDeAnalisis
from gramatica import gramatica
#from sintactico import analizador_sintactico # #
from tkinter import *
from tkinter import messagebox as MessageBox
import re
# ---------------------------------------------
import xlsxwriter
from tkinter import *    
from tkinter import ttk

t = tablaDeAnalisis()
g = gramatica()
 # #
listaAuxiliar = []
aux = []

class analizador_sintactico:
    
    def analizarSintaxis(self, palabras):
        s = analizador_sintactico()
        pila = ['ID']
        apuntador = 0
        bandera = True
        while True:
            cima = pila.pop()
            numPalabras = len(palabras)
            if(cima in g.noTerminales):  # NO TERMINAL
                print('Cima de la pila: ', cima)
                for clave in t.diccionario_tabla:
                    if(cima == clave): # ID 
                        print('Se elimina a: ', cima, 'de la Pila')
                        print('Se agregan reglas de: ', clave, 'a la Pila')
                        for dato in t.diccionario_tabla[clave]['regla']:
                            pila.append(dato)
                        print('Contenido de Pila: ',pila)
            else:  # TERMINAL
                if(cima == 'a...z'):
                    print('es una expresion regular (a...z|A...Z)')
                    resulExpresion = re.search("^[a-zA-Z][a-zA-Z]+$", palabras[apuntador])
                    if resulExpresion:
                        print('cumple la expresion')
                        cima = palabras[apuntador]
                    else:
                        print('Error de sintaxis: ', palabras[apuntador])
                        MessageBox.showerror("ERROR", "Error de sintaxis")
                        bandera = False
                        break
                if(cima == '0...9'):
                    print('es una expresion regular (0...9)')
                    resulExpresion = re.search("^[0-9]+$", palabras[apuntador])
                    if resulExpresion:
                        print('cumple la expresion')
                        cima = palabras[apuntador]
                    else:
                        print('Error de sintaxis: ', palabras[apuntador])
                        MessageBox.showerror("ERROR", "Error de sintaxis")
                        bandera = False
                        break
                if(cima == palabras[apuntador]):
                    apuntador += 1
                    print('Se extrae ', cima, ' de la pila') #
                    print('Contenido de Pila: ',pila)
                else:
                    print('Error de sintaxis: ', palabras[apuntador])
                    MessageBox.showerror("ERROR", "Error de sintaxis")
                    bandera = False
                    break
                if(len(pila) == 0):  # ----
                    print('PILA VACIA')
                    if(apuntador == numPalabras):
                        print('ENTRADA VACIA')
                        MessageBox.showinfo("CADENA VALIDA!", "ENTRADA VACIA Y PILA VACIA!")
                        # comprobaciones
                        s.comprobacion_semantica(palabras)
                        bandera = False
                        break
                    else:
                        print('ENTRADA CON DATOS')
                        MessageBox.showerror("CADENA NO VALIDA","ENTRADA CON DATOS")   
                        bandera = False
                        break  # ---
                if(apuntador == numPalabras):
                    print('ENTRADA VACIA')
                    MessageBox.showerror("ERROR", "Pila con datos, entrada vacia!")
                    print('Contenido de Pila: ', pila)
                    bandera = False
                    break
            if(bandera == False):
                break
    def comprobacion_semantica(self, palabras):
        print('Comprobaciones:')
        if(palabras[1] == palabras[20] and palabras[7] == palabras[25] and palabras[18] == palabras[23]):
            resulExpresion = re.search("^[A-Z][a-zA-Z]+$", palabras[1])
            if resulExpresion:
                #print('cumple la expresion')
                raiz = Tk()
                #print('clase cumple:')
                raiz.geometry('500x350')  # 1050x500
                raiz.configure(bg = '#49A') # '#0059b3' lightblue
                raiz.title('Diagrama de Clase') # width: ancho    height: alto
                ttk.Label(raiz, text=f"{palabras[1]}", width=43, background="#F0F8FF", foreground="black", font=("Arial", 15,)).place(y=10, x=10)
                ttk.Label(raiz, background='white', border=2).place(x=10,y=39, width=476, height=150) # cuadro arriba
                ttk.Label(raiz, text=f"{palabras[3]} " + ": entero").place(x=15,y=45)  #atributo 
                ttk.Label(raiz, text=f"{palabras[18]}" + " : " + f"{palabras[20]}").place(x=15,y=65)  # atributo instancia
                ttk.Label(raiz, background='white', border=2).place(x=10,y=191, width=476, height=150) # cuadro abajo
                ttk.Label(raiz, text=f"{palabras[7]}" + "()").place(x=15,y=199)
                raiz.mainloop()
            else:
                print('Primera letra de la clase NO es MAYUSCULA')
                MessageBox.showerror("ERROR NOMBRE DE CLASE", "La primera letra NO ES MAYUSCULA!")
        else:
            print('Error de Semantica!')
            MessageBox.showerror("ERROR SEMANTICA", "Los datos declarados, no son iguales!")
