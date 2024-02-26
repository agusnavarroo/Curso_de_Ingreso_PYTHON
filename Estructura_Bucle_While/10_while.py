import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativo = 0
        contador_negativo = 0
        acumulador_positivo = 0
        contador_positivo = 0
        contador_ceros = 0
        numero = prompt("Alerta", prompt = "Ingrese un numero")
        while numero != None :
            numero = int(numero)
            # A Y C
            if numero < 0 :
                acumulador_negativo +- numero
                contador_negativo +- 1
            
            # B Y D
            elif numero > 0 :
                acumulador_positivo += numero
                contador_positivo += 1

            # E
            
            else :
                contador_ceros += 1
            numero = prompt("Alerta", prompt = "Ingrese un numero")

        # F
                
        diferencia = contador_positivo - contador_negativo
        mensaje = "La suma acumulada de los negativos es {0}, la suma acumulada de los positivos es {1}, la cantidad de los numeros positivos ingresados es {2}, la cantidad de los numeros negativos ingresados es {3}, la cantidad de ceros es {4} y la diferencia entre numeros positivos y negativos es {5}".format(acumulador_negativo,acumulador_positivo,contador_negativo,contador_positivo,contador_ceros,diferencia)
        alert("Alerta", message = mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()