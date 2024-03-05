import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio_Extra_01
---
Enunciado:
Ingresar el valor del dólar oficial y el valor del dólar blue.
Mostrar la diferencia expresada en porcentaje entre una cotización y otra.

'''

dolar_oficial = "810"
dolar_blue = "1125"
dolar_oficial_numero = int(dolar_oficial)
dolar_blue_numero = int(dolar_blue)
diferencia_numero = (dolar_blue_numero - dolar_oficial_numero)
media_numero = (dolar_blue_numero + dolar_oficial_numero) /2
diferencia_porcentual = (diferencia_numero / media_numero) * 100
mensaje = "La diferencia porcentual es {0} %".format(diferencia_porcentual)
alert("Titulo", message = mensaje)