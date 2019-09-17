# ARCHIVOS (de texto)

# Abrir y Cerrar archivos

archivo_estudiantes = open("estudiantes.txt", "r")  # Así abrimos un archivo
print(archivo_estudiantes.read())
archivo_estudiantes.close()  # Así cerramos un archivo