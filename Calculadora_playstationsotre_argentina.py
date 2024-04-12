precio_juego_dolares = int(input("Ingresa el precio del juego que queres comprar en dolares: ")) # Pido valor del juego en dolares
valor_dolar = float(input("Ingresa el valor del dolar: ")) # Pido valor del dolar
precio_juego_pesos = precio_juego_dolares * valor_dolar # Transformo el valor del precio del juego en dolares a pesos
impuesto_iva = precio_juego_pesos * 0.21 # Calculo impuesto iva
impuesto_ganancias = precio_juego_pesos * 0.3 # Calculo impuesto a las ganancias
impuesto_pais = precio_juego_pesos * 0.08 # Calculo impuesto pais
impuesto_IIBB = precio_juego_pesos * 0.02 # Calculo impuesto capital, los de provincia comenten esta linea y borren el impuesto IIBB (igual solamente es un 2% menos)
precio_final_pesos = precio_juego_pesos + impuesto_iva + impuesto_ganancias + impuesto_pais + impuesto_IIBB
print(f"El precio final del juego en pesos es de {precio_final_pesos} pesos")


































# precio_juego_dolares = int(input("Coloque el precio del juego en dolares: "))
# valor_dolar = int(input("Coloque el precio del dolar: "))
# precio_juego_pesos = int(precio_juego_dolares) * int(valor_dolar)
# iva = precio_juego_pesos * (precio_juego_pesos * 0.21)
# impuesto_pais = precio_juego_pesos * (precio_juego_pesos * 0.08)
# impuesto_ganancias = precio_juego_pesos * (precio_juego_pesos * 0.30)
# #IIBB = int(precio_juego_pesos) (int(precio_juego_pesos) * 0.2)
# precio_final_pesos = precio_juego_pesos + iva + impuesto_ganancias + impuesto_pais
# print(f"El precio final del juego en pesos es de: {precio_final_pesos}")