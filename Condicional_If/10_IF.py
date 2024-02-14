import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Agustin
apellido: Navarro
---
Ejercicio: if_10
---
Enunciado:
Al presionar el botón 'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nota_random = random.randint(1,10)
        nota = str(nota_random)
        if nota_random >= 6 and nota_random <= 10 :
            alert("Nota", message="Promocion directa, la nota es " + nota)
        else : 
            if nota_random >= 4 and nota_random <= 5 :
                alert("Nota", message="Aprobado, la nota es " + nota)
            else : 
                if nota_random >= 1 and nota_random <= 3 :
                    alert("Nota", message="Desaprobado, la nota es " + nota)

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()