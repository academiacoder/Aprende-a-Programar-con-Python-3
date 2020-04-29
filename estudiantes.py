class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

        print(f"Se ha creado un estudiante llamado {self.nombre}")

    def desactivar(self):
        self.esta_activo = False

    def info(self):
        print(f"Estudiante: {self.nombre}\nEdad: {self.edad}\nActivo: {self.esta_activo}\n")

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
