# PROYECTO: Aplicar lo aprendido
# GUARDAR DATOS DE NUESTROS PROGRAMAS

import pickle

# Importamos nuestra clase estudiantes
from estudiantes import Estudiante as E


class ListaEstudiantes:
    estudiantes = []

    def __init__(self):
        archivoEstudiantes = open("lista_estudiantes", "ab+")
        archivoEstudiantes.seek(0)

        try:
            self.estudiantes = pickle.load(archivoEstudiantes)
            print(f"{len(self.estudiantes)} estudiante cargados correctamente del archivo externo")
        except EOFError:
            print("No se han cargado estudiantes previos")
        finally:
            archivoEstudiantes.close()
            del archivoEstudiantes


    def agregarEstudiante(self, e):
        self.estudiantes.append(e)
        self.guardarEstudiantes()

    def mostrarEstudiantes(self):
        for e in self.estudiantes:
            print(e)

    def guardarEstudiantes(self):
        archivo = open("lista_estudiantes", "wb")
        pickle.dump(self.estudiantes, archivo)
        archivo.close()
        del archivo


lista = ListaEstudiantes()

est1 = E("Benicio", 18, "Go")
est2 = E("Tiziana", 14, "C#")

lista.agregarEstudiante(est1)
lista.agregarEstudiante(est2)

lista.mostrarEstudiantes()

# TAREA PARA EL ESTUDIANTE
# Mejorar aún más el juego de Pokemon
# Una vez que termina una pelea de pokemon, guardar en un archivo externo que pokemon gano
# y sumarle 1 a las batallas ganadas de dicho pokemon
# Al finalizar una batalla nueva, que el programa nos indique cuantas batallas lleva ganadas
# dicho pokemon.
