# Ejemplo de promedio
suma_numeros = 0
contador = 0

print("Ingrese una serie de numeros para obtener su promedio. Ingrese 0 para finalizar.")

while True:
    numero = float(input("Ingrese un numero: "))

    if numero == 0:
        break

    suma_numeros += numero

    contador += 1

if contador > 0:
    promedio = suma_numeros / contador
    print("El promedio de los numeros ingresador es: ",promedio)

else:
    print("No se han ingresado numeros para calcular el promedio.")
