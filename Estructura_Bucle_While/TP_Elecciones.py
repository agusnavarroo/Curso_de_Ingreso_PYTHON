import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        bandera = 0
        suma = 0
        total_votos = 0
        contador = 0
        while True :
            nombre = prompt("Nombre", "Ingrese el nombre del candidato")
            if nombre == "" :
                alert("Alerta", "No se ingreso ningun nombre, vuelva a intentarlo")
                continue
            if nombre == None :
                break

            edad = prompt("Edad", "Ingrese la edad del candidato, debe ser mayor a 25 años")
            edad = int(edad)
            if edad < 25 :
                alert("Alerta", "La edad no puede ser menor a 25 años")
                continue

            suma += edad # Aca se suman las edades para, mas abajo, sacar el promedio como lo pide el enunciado

            votos = prompt("Votos", "Ingrese la cantidad de votos que tiene el candidato")
            votos = int(votos)
            if votos < 0 :
                alert("Alerta", "El candidato no puede tener menos de 0 votos, vuelva a intentarlo")
                continue 

            total_votos += votos # Lo mismo con los votos, para luego sumar la cantidad de votos total

            if bandera == 0 :
                maximo_votos = votos
                minimo_votos = votos
                nombre_max = nombre
                nombre_min = nombre
                edad_min = edad
                bandera = 1

            if votos < minimo_votos :
                minimo_votos = votos
                nombre_min = nombre
                edad_min = edad

            if votos > maximo_votos :
                maximo_votos = votos
                nombre_max = nombre

            contador += 1 # Cada vez que se cumpla todo el while, se suma 1 al contador que vendria a ser 1 candidato.

        promedio = suma / contador

        mensaje = "El candidato con mas votos es {0}, el candidato con menos votos es {1} de {2} años, el promedio de edad de los candidatos es de {3} años y la cantidad total de votos fue de {4} votos".format(nombre_max,nombre_min,edad_min,promedio,total_votos)
        alert("Resultados", message = mensaje)

            #continue

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()