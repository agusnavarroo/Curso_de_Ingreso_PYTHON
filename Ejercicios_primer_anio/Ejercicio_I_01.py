'''
nombre: Agustin
apellido: Navarro
---
Ejercicio: Integrador 1
---
Enunciado:
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.

Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
'''

contador_barbijos = 0
acumulador_jabon = 0

for i in range(5):

    tipo_producto = input("Ingrese el tipo de producto: Barbijo, Jabon o Alcohol:")
    while tipo_producto != "Barbijo" and tipo_producto != "Jabon" and tipo_producto != "Alcohol":
        tipo_producto = input("ERROR, Ingrese NUEVAMENTE el tipo de producto: Barbijo, Jabon o Alcohol: ")

    precio_producto = input("Ingrese el precio del producto: entre 100 y 300:")
    precio_producto = int(precio_producto)
    while precio_producto < 100 or precio_producto > 300:
        precio_producto = input("ERROR, Ingrese NUEVAMENTE el precio del producto: entre 100 y 300: ")
        precio_producto = int(precio_producto)

    unidades_producto = input("Ingrese las unidades compradas: mayor a 0 y menor a 1000: ")
    unidades_producto = int(unidades_producto)
    while unidades_producto < 1 or unidades_producto > 1000:
        unidades_producto = input("ERROR, Ingrese NUEVAMENTE las unidades compradas: mayor a 0 y menor a 1000: ")
        unidades_producto = int(unidades_producto)

    fabricante = input("Ingrese el nombre del fabricante :")

    match tipo_producto:
        case "Barbijo":
            if contador_barbijos == 0:
                barbijo_mas_caro = precio_producto
                cantidad_barbijo_mas_caro = unidades_producto
                fabricante_barbijo_mas_caro = fabricante

            else: 
                if barbijo_mas_caro < precio_producto:
                    barbijo_mas_caro = precio_producto
                    cantidad_barbijo_mas_caro = unidades_producto
                    fabricante_barbijo_mas_caro = fabricante

            contador_barbijos = contador_barbijos + 1

        case "Jabon":
            acumulador_jabon = acumulador_jabon + unidades_producto

    if i == 0:
        fabricante_mas_unidades = fabricante
        cantidad_producto_mas_unidades = unidades_producto
        producto_mas_unidades = tipo_producto

    else: 
        if cantidad_producto_mas_unidades < unidades_producto:
            fabricante_mas_unidades = fabricante
            cantidad_producto_mas_unidades = unidades_producto
            producto_mas_unidades = tipo_producto

print (f"El barbijo mas caro cuesta: {barbijo_mas_caro} con {cantidad_barbijo_mas_caro} unidades del fabricante {fabricante_barbijo_mas_caro}. El item con mas unidades es {producto_mas_unidades} del fabricante {fabricante_mas_unidades}. Hay un total de {acumulador_jabon} jabones en total")