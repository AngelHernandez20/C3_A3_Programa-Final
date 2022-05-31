from cProfile import label
from email.mime import image
from enum import auto
from tkinter import *    
from tkinter import ttk
from tkinter import messagebox
from tkinter import Frame
#from typing_extensions import Self
from analizadorlexico import analizador
#from analizador_L import analiza
import re
import os
import sys
#from tkinter import PhotoImage
raiz = Tk()
listbox = Listbox(raiz)
listbox.place(relx=0.25, rely=0.20, relheight=0.7, relwidth=0.5 )

a = analizador()

def datos():
  bandera = []
  listbox.delete(0, END)
  print(entrada.get())
  palabras = re.split("\s",entrada.get()) # se divide las palabras por cada espacio que encuentra
  bandera = a.inicio_analizador(palabras)
  print(bandera)
  items = (
    "-- Reservadas --",
    bandera[0],
    " ",
    "-- Caracteres especiales --",
    bandera[1],
    " ",
    "-- Delimitadores --",
    bandera[2],
    " ",
    "-- Indefinidas --",
    bandera[3],
    " ",
    "-- Digitos --",
    bandera[4],
    " ",
    "-- Errores --",
    bandera[5]
  )
  listbox.insert(0, *items)
  bandera.clear()
  #contador += 1

def reiniciar():
  print("REINICIO") 
  caja.delete(0, END)
  listbox.delete(0, END)

entrada = StringVar()
#entrada2 = StringVar()
# tamaño ventana
#raiz.resizable(False,False)
raiz.geometry('1050x500') 
# color fondo
raiz.configure(bg = 'lightblue')
# titulo 
raiz.title('Analizador lexico :) ')
#label.place(x=30,y=60)
#caja.place(x=70,y=150)
#imagen = PhotoImage(file = "Captura.png")
#background = Label(image = imagen)
#background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
caja = Entry(raiz,textvariable=entrada)
#a.inicio_analizador()
#a.inicio_analizador()
#caja = Entry(raiz,textvariable=entrada2).pack()
caja.place(x=278,y=57, width="500", height="35")
ttk.Button(raiz, text='Busqueda', command=datos).place(x=500,y=30, width="100",height="24")
ttk.Button(raiz, text='Reiniciar',command=reiniciar).place(x=800,y=250)
#.place(x=1000,y=600, width="100",height="24")
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
raiz.mainloop()