import pickle
from utilidades_extra import Estudiante

archivo_est = open("estudiantes_obj", "rb")

lista_estudiantes_obj = pickle.load(archivo_est)

for e in lista_estudiantes_obj:
    print(e.info())