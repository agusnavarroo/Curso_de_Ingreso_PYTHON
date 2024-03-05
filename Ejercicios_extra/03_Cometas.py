import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio_Extra_03
---
Enunciado: La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores

Todos los datos se ingresan por prompt. Pueden usar el mismo html del ejercicio 01 de E/S

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

AB = prompt("Prompt", prompt="Ingrese el largo del segmento AB (en cms)")
DC = prompt("Prompt", prompt="Ingrese el largo del segmento DC (en cms)")
BD = prompt("Prompt", prompt="Ingrese el largo del segmento BD (en cms)")
BC = prompt("Prompt", prompt="Ingrese el largo del segmento BC (en cms)")
AD = prompt("Prompt", prompt="Ingrese el largo del segmento AD (en cms)")
AC = prompt("Prompt", prompt="Ingrese el largo del segmento AC (en cms)")
metros_varillas = (float(AB) + float(DC) + float(BD) + float(BC) + float(AD) + float(AC)) / 100
area_romboide = (float(AB) * float(DC)) / 2
area_total = area_romboide + (area_romboide * 0.1)
area_rosa_azul = area_total / 2
mensaje = "Se necesitaran {0} mts de varillas de plastico y {1} metros de papel. Y {2} metros de papel rosa y {2} metros de papel azul para el cometa bicolor".format(metros_varillas,area_total,area_rosa_azul)
alert("Alerta", message = mensaje)

