# DECLARACIÓN IF (CONDICIONLES)
# Esta declaración condicional nos permite realizar una acción si una condición se cumple
# u otra acciión en caso de que no se cumpla


"""
EJEMPLO REAL:
Voy a salir,

SI hace calor,
    saldre en camiseta

SINO SI hace frio,
    saldré abrigado

SINO SI está lloviendo,
    llevaré paraguas

SINO
    me quedaré en casa
"""


si_es_hombre = False
eres_alto = False

"""
print("ANTES DEL IF\n")

if si_es_hombre and eres_alto:
    print("Eres un hombre alto")
elif si_es_hombre and not eres_alto :
    print("Eres un hombre bajo")
elif not si_es_hombre and eres_alto:
    print("No eres un hombre, pero eres alto")
else:
    print("No eres un hombre, y tampoco eres alto")

print("\nFUERA DEL IF")

# TAREA PARA LOS ALUMNOS PRACTICAR MUCHO UTILIZAR OR EN LUGAR DE AND, INVENTAR OTRA FORMA DE USAR
# TODOS LOS CONDICIONALES IF, ELIF Y ELSE
"""

# UTILIZANDO CONDICIONALES Y COMPARACIONES

"""




def mayor_edad(num):
    if num >= 18:
        return True
    else:
        return False


edad = input("Ingresa tu edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""


def mayor_numero(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


numero = mayor_numero(99, 556, 300)
print(numero)

# TAREA ESTUDIANTES: REALIZAR EJERCICIOS INVENTADOS PARA UTILIZAR CONDICIONALES Y COMPACIONES... MUCHOS!!!








