# Ejemplo de acumulador

acumulador = 0

while True :
    numero = int(input("Ingrese un numero. " "Ingrese el numero 0 para terminar: "))
    if numero == 0 :
        break # Salir del bucle si el numero ingresado es 0

    acumulador += numero

    
print("La suma de los numeros ingresados es: ", acumulador)

print("Fin del programa")