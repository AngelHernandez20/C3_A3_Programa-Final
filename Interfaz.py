from cProfile import label
#from email.mime import image
#from enum import auto
from tkinter import *    
from tkinter import ttk
#from tkinter import messagebox
from tkinter import Frame
from turtle import clear
from lexico import analizador_lexico
from sintactico import analizador_sintactico
import pandas as pd
import numpy as np
import re
raiz = Tk()
listbox = Listbox(raiz) #---
listbox.place(relx=0.25, rely=0.20, relheight=0.7, relwidth=0.5 ) #---

a = analizador_lexico()
s = analizador_sintactico()

def datos():
  bandera = []
  listbox.delete(0, END) #---
  print(entrada.get()) #---
  palabras = re.split("\s",entrada.get())
  palabrasAux = palabras[:] 
  bandera = a.analizarLexico(palabras) #--
  guardar_datosLexicos(bandera) #--
  s.analizarSintaxis(palabrasAux)
  bandera.clear()
  palabras.clear()
  palabrasAux.clear()

def guardar_datosLexicos(bandera):
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

def reiniciar():
  print("REINICIO") 
  caja.delete(0, END)
  listbox.delete(0, END) #---

entrada = StringVar()
raiz.geometry('1050x500')  # 1050x500
raiz.configure(bg = '#49A') # '#0059b3' lightblue
raiz.title('Analizador lexico :) ')
caja = Entry(raiz,textvariable=entrada)
caja.place(x=278,y=57, width="500", height="35")
ttk.Button(raiz, text='Busqueda', command=datos).place(x=500,y=30, width="100",height="24")
ttk.Button(raiz, text='Reiniciar',command=reiniciar).place(x=800,y=250) # x=800,y=250
#ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
raiz.mainloop()