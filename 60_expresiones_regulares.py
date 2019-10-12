# EXPRESIONES REGULARES o REGEX
# Módulo re

"""
Las expresiones regulares nos permiten trabajar con textos, más específicamente para
realizar busquedas de texto a través de métodos y utilizando una sintaxis propia
de la librería de expresiones regulares que utilicemos en cada lenguaje. Normalmente
la sintaxis utilizada para los patrones de búsqueda es compartida por la mayoría de
los lenguajes de programación.

PODEMOS UTILIZAR EXPRESIONES REGULARES PARA:
- Saber si existe una cadena de caracteres (palabra) dentro de un texto
- Conocer cuantes veces se encuentra una cadena de caracteres dentro de un texto
- Detectar si un texto se ajusta a un formato específico por ejemplo un
correo electrónico "texto" "@" "texto" "." "com" "." "ar"
- etc...
"""

import re

# Clase 1 - re.search
# Este método nos buscará la primer coincidencia de una cadena de caracteres dentro de un texto
# devolverá un objeto si es localizado o None si no es encontrado.

cadena = "Hola estudiantes de AcademiaCoder."

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)

print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.span())
print(a_buscar)














