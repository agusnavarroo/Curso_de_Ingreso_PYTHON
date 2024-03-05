import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio_Extra_02
---
Enunciado:
Para saber el costo de un viaje necesitamos el siguiente algoritmo,sabiendo que el precio por kilo de pasajero es 1000 pesos.
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso. Se pide  armar el siguiente mensaje
"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos

'''

nombre = prompt(title="Datos", prompt="Ingrese su nombre")
edad = prompt(title="Datos", prompt="Ingrese su edad")
edad_2 = prompt(title="Datos", prompt="Ingrese su edad")
peso = prompt(title="Datos", prompt="Ingrese su peso")
peso_2 = prompt(title="Datos", prompt="Ingrese su peso")
suma = float(peso) + float(peso_2)
promedio = (int(edad) + int(edad_2)) / 2
costo_viaje = suma * 1000
mensaje = "Hola {0}, sus pesos son {1} kilos y {2} kilos respectivamente, sumando da {3} kilos , el promedio de edad es {4} y su viaje vale {5} pesos".format(nombre,peso,peso_2,suma,promedio,costo_viaje)
alert("Alerta", message = mensaje)