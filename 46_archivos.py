# ARCHIVOS (de texto)

# Abrir y Cerrar archivos

archivo_estudiantes = open("estudiantes.txt", "a")  # Así abrimos un archivo
print(archivo_estudiantes.write("\nCarolina Massutti - ReactJS"))
archivo_estudiantes.close()  # Así cerramos un archivo

# Eliminar un archivo
