import random

while True :
    opciones = input("Atencion, Ingrese pieda papel o tijera o cancelar para terminar el juego: ")

    if opciones == "cancelar" :
        print("Gracias, hasta la proxima")
        break

    if opciones != "piedra" and opciones != "papel" and opciones != "tijera" :
        print("Error", "Solo podes ingresar piedra papel o tijera")
        continue

cpu = random.choice("piedra","papel","tijera")
