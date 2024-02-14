from customtkinter import *

app = CTk()

def buttom_on_click():
    print ("Vamos a aprender python!!")

    buttom = CTkButton(master=app, text="Click me!", command=buttom_on_click)
    buttom.grid()

    app.mainloop() 