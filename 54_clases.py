# CLASES Y OBJETOS


class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

    def desactivar(self):
        self.esta_activo = False


estudiante1 = Estudiante("Marcos", 35, "Python")


print(estudiante1.esta_activo)

estudiante1.desactivar()

print(estudiante1.esta_activo)

# TAREA PARA EL ESTUDIANTE.
# Crear 2 métodos:
# 1 que permita añadir cursos a los que el estudiante se ha inscripto
# 2 otro método que permita eliminar cursos del estudiante
