#saludo = "Hola Mundo" #Variable Local

#print(saludo)

# Funciones Arriba

# def saludar(): #Declaracion
#     print("Hola Mundo") # Desarrollo

# Desarrollo de la app abajo
#saludar() # Si pongo esto llamo  a la funcion saludar, si pongo dos lineas mas de saludar, llama a las funcion 3 veces e imprime hola mundo tres veces

def imprimir_texto(mensaje:str) : #Declaro pero con la variable mensaje, y el :str es para indicar el tipo de variable
    print(mensaje)

# Desarrollo de la app abajo
# imprimir_texto("Hola division 314") # Aca y abajo le agrego valor a la variable mensaje, de tipo str, si llamo me muestra ambos print
# imprimir_texto("Hola mundo")

# Creando una funcion sumar

# Aca estan los parametros formales (numero_uno y numero_dos)
def suma(numero_uno:int,numero_dos:int) : # Entradas
    '''
    ESTO ES LA DOCUMENTACION
    Esta funcion se encarga de sumar dos numeros enteros
    Recibe el primer numero, representando el numero 1
    Recibe el segundo numero, representando el numero 2
    Retorna la suma entre los dos numeros
    '''
    # El proceso es la suma entre los dos numeros
    return numero_dos + numero_dos # Salida

# Usando la funcion
# Aca estan los parametros actuales (11 y 22)
resultado = suma(11,22)
print(f"El resultado es {resultado}")