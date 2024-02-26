# Ejemplo de incremento pero mas lento

import time

numero = 1

while numero <= 5 : # Se ejecuta mientras numero <= 5
    print(numero)
    numero +=1 # Imprime todos los numeros, sumando cada vez 1 hasta llegar al 6, que es cuando la condicion deja de ser verdadera.
    time.sleep(5) # Imprime el numero cada 5 segundos