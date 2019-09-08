# ADIVINA EL NÚMERO 1.0

import random

# Generamos un número aleatorio entre 1 y 10
adivina = random.randint(1, 20)

print("Hola, Cómo te llamas?")
nombre = input()

print("Muy bien " + nombre + " estoy pensando un número entre 1 y 20, intenta adivinarlo")
print("A proposito, solo tienes 3 posibilidades")

num = int(input("Intenta adivinar: "))

if num == adivina:
    print("GANASTE!")
else:
    if num > adivina:
        print("Intenta con un número más pequeño")
    else:
        print("Intenta con un número más grande")

    print("\nTe quedan 2 intentos")
    num = int(input("Intenta otra vez: "))

    if num == adivina:
        print("GANASTE!")
    else:
        if num > adivina:
            print("Intenta con un número más pequeño")
        else:
            print("Intenta con un número más grande")

        print("\nTe queda 1 intento")
        num = int(input("Intenta otra vez: "))

        if num == adivina:
            print("GANASTE!")
        else:
            print("PERDISTE")






