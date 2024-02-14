import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto para luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)  # El .grid ordena

        self.label2 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)

        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=1, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        datos = self.txt_nombre.get() + self.txt_apellido.get()
        alert(title="Alerta", message="Tu nombre es " + datos)

# Una manera mas profesional de escribir la linea 38 seria: saludo = "Hola {} {}, trabajas en {} y vivis en {}" Las {} son las variables
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()