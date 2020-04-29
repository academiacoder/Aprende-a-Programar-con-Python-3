import random

metros_en_kilometro = 1000
super_heroes = ["Thor", "IronMan", "Hulk", "Wolverine"]


def tomar_extension(filename):
    return filename[filename.index(".") + 1:]


def tirar_dado(num):
    return random.randint(1, num)


class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

    def desactivar(self):
        self.esta_activo = False

    def info(self):
        print(f"Estudiante: {self.nombre}\nEdad: {self.edad}\nActivo: {self.esta_activo}\n")
