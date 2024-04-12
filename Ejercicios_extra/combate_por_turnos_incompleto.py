import random
import time

# 2 pokemon, 100 hp, combate por turnos hasta que la la vida de alguno llegue a 0
# generar un numero random entre 10/20 (poder de ataque)
# turno de combate(actual) el pokemon ataca con cuantos puntos ataca, vida restante del rival

bandera = False
pikachu = 100
evee = 100
turno = 0

while pikachu > 0 and evee > 0 :
    if turno % 2 == 0 :
            ataque = random.randint(10,20)
            evee -= ataque
            print(f"Atencion, pikachu quita {ataque} de vida, la vida de eeve es {evee} hp")
    if turno % 2 != 0 :
            ataque = random.randint(10,20)
            pikachu -= ataque
            print(f"Atencion, evee quita {ataque} de vida, la vida de pikachu es {pikachu} hp")
            time.sleep(2)
    turno += 1

if pikachu <= 0 :
    print("Eeve gana el combate")

else: 
    print("Pikachu gana el combate")