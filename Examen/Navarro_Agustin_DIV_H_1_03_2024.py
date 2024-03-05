import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Enunciado:
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos:

Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
Informe C- La marca y tipo del contenedor más costoso
Informe D- La marca del contenedor de aluminio con mayor costo
Informe E- El promedio de costo de todos los contenedores

"""
contenedores = 0
contador_aluminio = 0
contador_hierro = 0
contador_madera = 0
contador_peligroso = 0
contador_comestible = 0
contador_indumentaria = 0
bandera = 0
marca_contenedor_mas_costoso = ""
tipo_material_punto_c = ""
costo_contenedor_mas_costoso = 0
bandera_1 = 0
marca_contenedor_aluminio_mas_costoso = ""
costo_contenedor_aluminio_mas_costoso = 0
suma_costo_contenedores = 0

for contenedores in range (1,21) :
    marca = prompt ("Alerta", prompt = "Indique la marca del contenedor")
    categoria = prompt ("Alerta", prompt = "Indique la categoria del contenedor, debe ser peligroso, comestible o indumentaria")
    while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria" :
        print("Error", "Categoria del contenedor no valida, reintente")
        categoria = prompt ("Alerta", prompt = "Indique la categoria del contenedor, debe ser peligroso, comestible o indumentaria")
    peso = prompt ("Alerta", prompt = "Indique el peso del contenedor, debe ser entre 100 y 800 kg")
    peso = float(peso)
    while peso < 100 or peso > 800 :
        print("Error", "Peso del contenedor no valido, reintente")
        peso = prompt ("Alerta", prompt = "Indique el peso del contenedor, debe ser entre 100 y 800 kg")
        peso = float(peso)
    tipo_de_material = prompt ("Alerta", prompt = "Indique el tipo de material del contenedor, debe ser aluminio, hierro o madera")
    while tipo_de_material != "aluminio" and tipo_de_material != "hierro" and tipo_de_material != "madera" :
        print("Error", "Tipo de material del contenedor no valido, reintente")
        tipo_de_material = prompt ("Alerta", prompt = "Indique el tipo de material del contenedor, debe ser aluminio, hierro o madera")
    costo = prompt ("Alerta", prompt = "Indique el costo del contenedor, debe ser mayor a 0")
    costo = float(costo)
    while costo <= 0 :
        print("Error", "Costo del contenedor no valido, reintente")
        costo = prompt ("Alerta", prompt = "Indique el costo del contenedor, debe ser mayor a 0")
        costo = float(costo)
    suma_costo_contenedores += costo
    contenedores += 1

    # Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
    match tipo_de_material :
        case "aluminio" :
            contador_aluminio += 1
            # Informe D- La marca del contenedor de aluminio con mayor costo
            if bandera_1 == 0 :
                marca_contenedor_aluminio_mas_costoso = marca
                costo_contenedor_aluminio_mas_costoso = costo
                bandera_1 = 1

            elif costo > costo_contenedor_aluminio_mas_costoso :
                marca_contenedor_aluminio_mas_costoso = marca
                costo_contenedor_aluminio_mas_costoso = costo

        case "hierro" :
            contador_hierro += 1

        case _:
            contador_madera += 1

    if contador_aluminio < contador_hierro and contador_aluminio < contador_madera :
        material_menos_usado = "El tipo de material menos usado fue el aluminio"

    if contador_hierro < contador_aluminio and contador_hierro < contador_madera :
        material_menos_usado = "El tipo de material menos usado fue el hierro"
    
    else: 
        material_menos_usado = "El tipo de material menos usado fue la madera"

    #Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
    match categoria :
        case "peligroso" :
            contador_peligroso += 1
        
        case "comestible" :
            contador_comestible += 1

        case _:
            contador_indumentaria += 1
#Informe C- La marca y tipo del contenedor más costoso
    if bandera == 0 :
        marca_contenedor_mas_costoso = marca
        tipo_material_punto_c = tipo_de_material
        costo_contenedor_mas_costoso = costo
        bandera = 1
    
    if costo > costo_contenedor_mas_costoso :
        marca_contenedor_mas_costoso = marca
        tipo_material_punto_c = tipo_de_material
        costo_contenedor_mas_costoso = costo

#Informe E- El promedio de costo de todos los contenedores


if contador_peligroso > 0 :
        porcentaje_categoria_peligroso = (contador_peligroso * 100) / 20

if contador_comestible > 0 :
        porcentaje_categoria_comestible = (contador_comestible * 100) / 20

if contador_indumentaria > 0 :
        porcentaje_categoria_indumentaria = (contador_indumentaria * 100) / 20

promedio_costo_contenedodres = suma_costo_contenedores / 20


print(f"{material_menos_usado}, el porcentaje de categoria peligroso es de {porcentaje_categoria_peligroso} %, el porcentaje de categoria comestible es de {porcentaje_categoria_comestible} %, el porcentaje de categoria indumentaria es de {porcentaje_categoria_indumentaria} %, la marca del contenedor mas costoso es {marca_contenedor_mas_costoso} del tipo {tipo_material_punto_c}, la marca del contenedor de aluminio con mayor costo es {marca_contenedor_aluminio_mas_costoso} y el promedio de costo de todos los contenedores es de {promedio_costo_contenedodres} pesos")

