caracter_elegido = "x"


def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra in "AEIOUÁÉÍÓÚaeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada


while True:
    print(encriptar(input("Ingresa una frase: "), input("Ingresa caracter que va a reemplazar")))

    print("\n Ingresa: \n 1 para encriptar otra fase ")
    print(" 2 para finalizar \n")

    opcion = input("")

    if opcion == "2":
        print("Gracias por participar")
        break
    if opcion == "1":
        print("----0----")

    else:
        while True:
            print("Ingresa una opción válida")
            print(" 1 Para encriptar otra fase ")
            print(" 2 Para finalizar \n")
            opcion = input("")
            break