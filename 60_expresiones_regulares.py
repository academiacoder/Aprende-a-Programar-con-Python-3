# coding=utf-8
# EXPRESIONES REGULARES o REGEX
# Módulo re

"""
DOCUMENTACIÓN OFICIAL
https://docs.python.org/3.7/library/re.html
"""

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

cadena = "Hola estudiantes de AcademiaCoder. En AcademiaCoder los estudiantes aprenderan programación."

cadena2 = """
Hola estudiantes de AcademiaCoder.
En AcademiaCoder los estudiantes aprenderan programación.
Recuerden que nos centramos en el Desarrollo Web
"""

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)

"""
print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.span())
print(a_buscar)
"""
# Clase 2 - re.findall, re.split, re.sub
# En esta clase aprenderemos a utilizar estos métodos de la librería re
"""
re_findall = re.findall(a_buscar, cadena)
print(re_findall)

re_split = re.split("\s", cadena)
print(re_split)

re_sub = re.sub(a_buscar, "desarrolladores", cadena)
print(re_sub)


print(cadena2)
"""


# Clase 3 - Anclas y Metacaracteres (Sintaxis de RegEx)
# ^, $, []

lista = [
    "Marcos - Python",
    "Carlos - JavaScript",
    "Ana - JavaScript",
    "Marcos - PHP",
    "Natalia - Vue",
    "Violeta - Python",
    "Ana - Vue",
    "Carla - PHP",
    "Marcos - Programacion",
    "Benicio - Programación"
]

# Quitar las comillas triples para probar el código de la clase 3 de Expresiones regulares
"""
for linea in lista:
    if re.findall('Programaci[oó]n', linea):
        print(linea)
"""

# Clase 4 - Rangos, Rango Negado, Clases Predefinidas, Cuantificadores y Otros Metacaracteres

# Rangos []

# [a-d] esto significaría que buscamos cualquier letra comprendida entre a y d es decir "abcd"


# [0-7] esto significaría que buscamos cualquier número comprendido entre 0 y 7 es decir "01234567"

# Rango Negado ^

cadena = "abcdef ghi" \
         "0123456789-"
# Clases Predefinidas

# \d corresponde a [0-9]
# \w todas las letras minus., mayus., números y guiones bajos
# \s corresponde a espacios en blanco (espacio, tabulaciones, nuevas lineas...)

"""
CUANTIFICADORES

Son caracteres que multiplican el patrón que les precede.
Mientras que con las clases de caracteres podemos buscar un dígito, o una letra; 
con los cuantificadores podemos buscar cero o más letras, al menos 7 dígitos, o entre tres y 
cinco letras mayúsculas. Los cuantificadores son:

?: coincide con cero o una ocurrencia del patrón. Dicho de otra forma, hace que el patrón sea opcional
+: coincide con una o más ocurrencias del patrón
*: coincide con cero o más ocurrencias del patrón.
{x}: coincide con exactamente x ocurrencias del patrón
{x, y}: coincide con al menos x y no más de y ocurrencias. Si se omite x, el mínimo es cero, y si se omite y, no hay máximo. Esto permite especificar a los otros como casos particulares: ? es {0,1}, + es {1,} y * es {,} o {0,}.
Ejemplos:

.* : cualquier cadena, de cualquier largo (incluyendo una cadena vacía)
[a-z]{3,6}: entre 3 y 6 letras minúsculas
\d{4,}: al menos 4 dígitos
.*[hH]ola!?: una cadena cualquiera, seguida de hola, y terminando (o no) con un !
"Mi nombre es Marcos, hola!"
"Mi nombre es Marcos, hola"
OTROS METACARACTERES
Existen otros metacaracteres en el lenguaje de las expresiones regulares:

?: Además de servir como cuantificador, puede modificar el comportamiento de otro. 
De forma predeterminada, un cuantificador coincide con la mayor cadena posible. 
Cuando se le coloca un ?, se indica que se debe coincidir con la menor cadena posible. 
Esto es: dada la cadena bbbbb, b+ coincide con la cadena entera, mientras que b+? coincide solamente con b. 
Es decir, la menor cadena que cumple el patrón.

(): agrupan patrones. Sirven para que aquel pedazo de la cadena que coincida con el patrón sea capturado; 
o para delimitar el alcance de un cuantificador. Ejemplo: ab+ coincide con ab, abb, abbbbb, …, 
mientras que (ab)+ coincide con ab, abab, abab…

| : permite definir opciones para el patrón: perro|gato coincide con perro y con gato.
"""
