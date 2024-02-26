# Ejemplo de validacion de numero
while True :
    numero = int(input("Ingrese un numero positivo: ")) # Le pedimos al usuario que ingrese un numero tipo string y lo transformamos a
    if numero <= 0 :
        print("El numero ingresado no es positivo, reintente.")
        continue #El continue omite todo lo que este abajo de el y vuelve al while
    
    # No hace falta un if ni un numero >= 0 aca porque ya se sabe que va a ser mayor o igual a 0
    
    print("El numero ingresado es positivo")
    break # Finaliza el while si se cumple la condicion y sigue con lo de abajo

print("Fin del programa")