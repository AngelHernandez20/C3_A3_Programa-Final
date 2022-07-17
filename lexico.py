from calendar import c
from doctest import master
from multiprocessing.reduction import duplicate
import re
import string
from struct import pack
from unittest import result
from tokens import tokens
from tkinter import *    
from tkinter import ttk

resultReservadas = []
resultCaracteresEspeciales = []
resultDelimitadores = []
resultIndefinidas = []
resultErrores = []
resultDigitos = []
listResultados = []

class analizador_lexico:

    tokens = tokens()

    def analizarLexico(self, palabras):
        resultReservadas = []
        resultCaracteresEspeciales = []
        resultDelimitadores = []
        resultDigitos = []
        resultIndefinidas = []
        resultErrores = []
        print("--- Lexico ---")
        for i in tokens.reservadas:
            for j in palabras:
                if (i == j):
                    resultReservadas.append(i)
                    palabras.remove(i)
        for l in tokens.caracteres_especiales:
            for k in palabras:
                if (l == k):
                    resultCaracteresEspeciales.append(k)
                    palabras.remove(l)
        for t in tokens.delimitadores:
            for f in palabras:
                if (t == f):
                    resultDelimitadores.append(t)
                    palabras.remove(t)
        for g in range (len(palabras)):
            #dato = re.search("^[A-Za-z]+$*", palabras[g])
            dato = re.search("^[a-zA-Z][a-zA-Z]+$", palabras[g])
            if dato:
                resultIndefinidas.append(palabras[g])
            else:
                dato1 = re.search("^[0-9]+$", palabras[g])
                if dato1:
                    resultDigitos.append(palabras[g])
                else:
                    resultErrores.append(palabras[g])
        print("Token Reservadas: ",resultReservadas)
        print("Token Caracteres Especiales: ",resultCaracteresEspeciales)
        print("Token Delimitadores: ",resultDelimitadores)
        print("Token Indefinidas: ",resultIndefinidas)
        print("Token Digitos: ",resultDigitos)
        print("Errores: ",resultErrores)
        listResultados.append(resultReservadas)
        listResultados.append(resultCaracteresEspeciales)
        listResultados.append(resultDelimitadores)
        listResultados.append(resultIndefinidas)
        listResultados.append(resultDigitos)
        listResultados.append(resultErrores)
        return listResultados
