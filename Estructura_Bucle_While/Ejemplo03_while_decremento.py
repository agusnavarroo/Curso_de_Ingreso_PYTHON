# Ejemplo de decremento



contador = 0

while True :
    numero = int(input("Ingrese un numero. " "Ingrese un numero negativo para terminar: "))
    if numero <= 0 :
        break
    contador +=1 # Incrementamos uno, si el numero es positivo, se incrementa 1

    
print("Has ingresado", contador, "numero positivos")