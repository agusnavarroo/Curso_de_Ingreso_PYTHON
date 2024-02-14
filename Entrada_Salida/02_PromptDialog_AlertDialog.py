import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''
int_valor = 0
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")       # Esta linea de codigo le pone titulo a la ventana principal
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)  # Esta linea es para declarar/agregar un boton
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew") # Esta linea posiciona el boton en la ventana principal, row es la fila, pady determina a cuanto espacio de los bordes se coloca el boton, columspan es en que columna se posiciona el boton,  sticky="nsew" dice que el boton puede expandirse todo lo que la celda le permita


    def btn_mostrar_on_click(self):
        int_valor = prompt(title="Prompt",prompt="Introduzca un valor")
        alert(title="Alerta", message="Tu valor ingresado es: " + int_valor)
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()