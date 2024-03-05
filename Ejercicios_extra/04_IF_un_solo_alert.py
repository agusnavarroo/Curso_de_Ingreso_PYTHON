import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Agustin
apellido: Navarro
---
Ejercicio_Extra_04
---
Enunciado: Ejercicio 07 BIS V1 (Realizar en los archivos  del ejercicio 07 del IF)
1.Si es menor de 13 , mostrar el mensaje “feliz día”.
2.Si es adolescente el mensaje es “usted es adolescente”
 a.Si tiene 17 años además mostrar el mensaje “último año!!!”
3.Si es mayor de edad mostrar el mensaje “tenes edad de laburar”.
 a.Si tiene 33 años , además mostrar el mensaje “como cristo”
 b.Si tiene más de 60 años, además mostrar el mensaje “A jubilarse”.
 c.Si tiene 88, además mostrar el mensaje “lindo número''
4.Si la edad es par , además mostrar , “sos par!!”.

'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad = self.txt_edad.get()
        edad_numero = int(edad)
        par = edad_numero % 2
        if edad_numero < 13 :
            mensaje = "Feliz Dia"
        elif edad_numero >= 13 and edad_numero < 17 :
            mensaje = ("Usted es adolescente")
        elif edad_numero == 17 :
            mensaje = ("Usted es adolescente, ultimo año!!!")
        elif edad_numero >=18 and edad_numero <= 32 :
            mensaje = ("Tenes edad de laburar")
        elif edad_numero == 33 :
            mensaje = ("Tenes edad de laburar, como cristo")
        elif edad_numero > 60 and edad_numero <= 87 :
            mensaje = ("Tenes edad de laburar, como cristo, a jubilarse")
        elif edad_numero == 88 :
            mensaje = ("Tenes edad de laburar, como cristo, a jubilarse, lindo numero")

        alert("Alerta", message = mensaje)
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
'''
    if edad_numero < 13 :
            alert("Alerta", message = "Feliz Dia")
        elif edad_numero >= 13 and edad_numero < 17 :
            alert("Alerta", message = "Usted es adolescente")
        elif edad_numero == 17 :
            alert("Alerta", message = "Usted es adolescente, ultimo anio!!!")
        elif edad_numero >=18 and edad_numero <= 32 :
            alert("Alerta", message = "Tenes edad de laburar")
        elif edad_numero == 33 :
            alert("Alerta", message = "Tenes edad de laburar, como cristo")
        elif edad_numero > 60 and edad_numero <= 87 :
            alert("Alerta", message = "Tenes edad de laburar, como cristo, a jubilarse")
        elif edad_numero > 88 :
            alert("Alerta", message = "Tenes edad de laburar, como cristo, a jubilarse, lindo numero")

'''