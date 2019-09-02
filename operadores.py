# Los operadores son signos, símbolos o palabras que el interprete utiliza para hacer una operación específica

# OPERADORES MATEMÁTICOS
"""
+ Operador de Suma
- Operador de Resta
- Operador de Negativo
* Operador de Multiplicación
** Operador de Exponente
/ Operador de División
// Operador de División Entera
% Operador de Módulo o Resto
"""

# Reglas de precedencia de las operaciones matemáticas
"""
En orden de precedencia
1. Parentesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Resta
"""

numero1 = 10
numero2 = 5

# Realizar todas las operaciones aritméticas utilizando estos 2 números!

resultado = 12 * 5 + 2 / 3 ** 2
# print(resultado)

resultado1= (12 * 5) + (2 / (3 ** 2))
# print(resultado1)

resultado2 = (12 * 5) + (2 / 3) ** 2
# print(resultado2)


# OPERADORES PARA CADENAS
"""
+ Operador de Concatenación
* Operador de Repetición
"""

cadena1 = "Hola "
cadena2 = "mundo"

cadenas_unidas = cadena1 + cadena2

# print(cadenas_unidas)

cadenas_repetidas = cadena1 * 3

# print(cadenas_repetidas)


# OPERADORES DE RELACIÓN
# Los operadores de relación evaluan si 2 valores u objetos cumplen con una condición.
# El resultado de dicha evaluación es un objeto booleano (bool)
"""
== ¿Igual A?
!= ¿Distinto de?
> ¿Mayor que?
< ¿Menor que?
>= ¿Mayor o Igual que?
<= ¿Menor o Igual que?
"""

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5
numero_cadena = "10"

igual = numero1 == numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print

distinto = numero1 != numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print

mayor_que = numero1 > numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print

menor_que = numero1 < numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print

mayor_igual = numero1 >= numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print

menor_igual = numero1 >= numero2
# Tarea hacer todas las comprobaciones con los distintos números y su respectivo print


# OPERADORES DE ASIGNACIÓN
# Los operadores de asignación se utilizan para asignar un valor a una variable
"""
= Asignación simple -> x = y
+= Asignación suma -> x += y equivale a x = x + y
-= Asignación resta -> x -= y equivale a x = x - y
*= Asignación multiplicación -> x *= y equivale a x = x * y
**= Asignación exponente -> x **= y equivale a x = x ** y
/= Asignación división -> x /= y equivale a x = x / y
//= Asignación división entera -> x //= y equivale a x = x // y
%= Asignación división entera -> x %= y equivale a x = x % y
"""

numero1 = 1
numero2 = 2
# Podemos asignar varios valores en una misma linea
numero3, numero4, numero5 = 3, 4, 5

# Asignación suma
numero1 = numero1 + numero2
# print(numero1)
numero1 = 1
numero1 += numero2
# print(numero1)

# Asignación resta
numero1 = 1
numero1 = numero1 - numero2
# print(numero1)
numero1 = 1
numero1 -= numero2
# print(numero1)

# Escribir todas las asignaciones restantes

# ¿Alguien me podría explicar cómo funciona esta linea de código?
# a, b = b, a + b

a = 1
b = 2

a, b = b, a + b
# print(a, b)

a = 1
b = 2
# print(a, "valor de A")
a = b
# print(a, "valor de A luego de asignarle B")
b = a + b
# print(a, b)

