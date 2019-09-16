# ENCRIPTADOR DE FRASES

# "Hola AcademiaCoder, ¿Cómo están hoy?"
# Caracter elegido "xX"
# "Hxlx XcxdxmxxCxdxr, ¿Cxmx xstxn hxy?"

# Variables para modificar el programa
caracter_elegido = "x"


def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada


while True:
    print(encriptar(input("Ingresa una frase:\n>"), caracter_elegido))

    print("\nIngresa:\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input(">")
    if opcion == "2":
        print("HASTA LUEGO!!!")
        break
    if opcion == "1":
        print("----O----\n")

# TAREA PARA LOS ESTUDIANTES:
# 1 - Hacer que el usuario pueda decidir que letra utilizar para encriptar
# 2 - Jugar con el código y hacer más intereante el encriptador.
# Por ejemplo: hacer algo para identificar que se encriptaron caracteres con acento.





