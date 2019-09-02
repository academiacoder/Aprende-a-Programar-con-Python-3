# JUEGO HISTORIA LOCA
# http://www.educandolectores.es/2018/07/02/mad-libs-o-historias-locas-un-juego-de-palabras-muy-divertido/

print("CREA TU HISTORIA LOCA")
print("Ingresa las palabras que te solicitamos:\n")
# Declaramos las variables
# utilizando input para que el usuario ingrese lo que pedimos
pal1 = input("Parte del cuerpo en plural: ")
pal2 = input("Adjetivo en plural: ")
pal3 = input("Adjetivo: ")
pal4 = input("Adjetivo: ")
pal5 = input("Nombre propio: ")

print("\nESTA ES LA HISTORIA QUE HAS CREADO:")
# Impirimimos la historia por pantalla
print(f"Antiguamente, el ser humano caminaba a cuatro {pal1.lower()},")
print(f"se expresaba mediante gruñidos {pal2} y no sabía encender")
print(f"un {pal3} fuego. Esta es la historia del día en que la humanidad")
print(f"cambió para siempre (traducida del {pal4} idioma de las cavernas):")
# TAREA PARA EL ESTUDIANTE: Completar la historia o inventar una nueva
print(f"El nombre era {pal5.capitalize()}")  # Esta linea no pertece a la historia CAMBIALA!!!
