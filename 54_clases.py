# CLASES Y OBJETOS


class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]


estudiante1 = Estudiante("Marcos", 35, "Python")

estudiante1.edad = 36

print(estudiante1.apellido)