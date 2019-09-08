# VERSIÓN 2.0 DE ADIVINAS EL NÚMERO

import random

# Variables para modificar el juego
posibilidades = 5
limite = 10

print("Hola, Cómo te llamas?")
nombre = input()

print("Muy bien " + nombre + " estoy pensando un número entre 1 y " + str(limite) +", intenta adivinarlo")
print("A proposito, solo tienes " + str(posibilidades) + " posibilidades")

# Generamos un número aleatorio entre 1 y 10
adivina = random.randint(1, limite)

intentos = 0
while intentos < posibilidades:

    num = int(input("Intenta adivinar: "))

    if num == adivina:
        print("GANASTE!")
        break
    else:
        if num > adivina:
            print("Intenta con un número más pequeño")
        else:
            print("Intenta con un número más grande")
    intentos += 1

if num != adivina:
    print("PERDISTE")



