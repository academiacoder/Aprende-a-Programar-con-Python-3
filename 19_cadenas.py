# TRABAJAMOS CON CADENAS DE TEXTO

# Las cadenas pueden tratarse como listas
cadena = "Hola AcademiaCoder prueba"

# H o l a   A c a d e m  i  a  C  o  d  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

letra = cadena[5]
# print(letra)

letra = cadena[-18]
# print(letra)

letras = cadena[:2]
# print(letras)


# FUNCIONES DE LAS CADENAS DE TEXTO
# Tienen todas las funciones en https://docs.python.org/3/library/stdtypes.html#string-methods

modificada = cadena.split()
# print(modificada)

cadena_con_comas = "Marcos,Natalia,Tiziana,Benicio"
lista_nombres = cadena_con_comas.split(',')
# print(lista_nombres)


# UNIENDO VARIABLES Y CADENAS
alumnos = 2500
academia = "AcademiaCoder"

cadena = "Los " + str(alumnos) + " alumnos de " + academia + " son muy aplicados"
# print(cadena)

# .format
cadena = "Los {} alumnos de {} son muy aplicados".format(alumnos, academia)
# print(cadena)

cadena = "Los {a} alumnos de {b} son muy aplicados".format(a=alumnos, b=academia)
# print(cadena)

cadena = f"Los {alumnos} alumnos de {academia} son muy aplicados"
# print(cadena)


# INTRODUCIR TEXTO POR TECLADO
# la función de python que nos permite introducir texto es input()
# print("Ingresa tu Nombre:")
# nombre = input()

nombre = input("Ingresa tu Nombre: ")
print(f"El alumno se llama {nombre}")



