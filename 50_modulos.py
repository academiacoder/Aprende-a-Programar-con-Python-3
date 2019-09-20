import random
from docx import Document
from utilidades_extra import tirar_dado as td

# MODULOS

# Un módulo es un archivo que podemos importar dentro de un archivo en el cual
# estamos trabajando y hacer uso de su contenido, como funciones y variables.

print(td(6))

print(random.randint(10, 15))

# PIP
# Gestor de paquetes, gestor de módulos o librerias creadas por terceros.

document = Document()


