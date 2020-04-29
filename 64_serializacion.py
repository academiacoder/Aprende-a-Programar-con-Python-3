# SERIALIZACIÓN
"""
Serialización  es el proceso de convertir un objeto en una secuencia de bytes para almacenarlo
o transmitirlo a la memoria, a una base de datos o a un archivo.
Su proposito principal es guardar el estado de un objeto para poder voler a crearlo cuando sea
necesario. El proceso inverso se denomina deserialización.

FUENTE: https://docs.microsoft.com/es-es/dotnet/csharp/programming-guide/concepts/serialization/
"""

# PARA SERIALIZAR EN PYTHON UTILIZAREMOS LA LIBRERÍA "PICKLE"
import pickle

# 1. SERIALIZAR COLECCIONES
"""estudiantes = [
    "Marcos",
    "Carla",
    "Agustín",
    "Pedro",
    "María"
]

archivo_serializado = open("estudiantes", "wb")  # Creamos un archivo para guardar el estado

pickle.dump(estudiantes, archivo_serializado)  # Volcamos el contenido de la lista en el archio

archivo_serializado.close()
del archivo_serializado

archivo = open("estudiantes", "rb")

lista_estudiantes = pickle.load(archivo)

print(lista_estudiantes)

for e in lista_estudiantes:
    print(e)"""


# 1. SERIALIZAR OBJETOS

from utilidades_extra import Estudiante


"""est1 = Estudiante("Marcos", 35, "Python")
est2 = Estudiante("Carla", 19, "JS")
est3 = Estudiante("Pedro", 26, "C#")

lista_est_obj = [
    est1,
    est2,
    est3
]

archivo_est_obj = open("estudiantes_obj", "wb")  # Creamos un archivo para guardar el estado

pickle.dump(lista_est_obj, archivo_est_obj)  # Volcamos el contenido de la lista en el archio

archivo_est_obj.close()
del archivo_est_obj"""


archivo_est = open("estudiantes_obj", "rb")

lista_estudiantes_obj = pickle.load(archivo_est)

for e in lista_estudiantes_obj:
    print(e.info())




