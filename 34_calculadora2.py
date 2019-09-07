# MEJORANDO NUESTRA CALCULADORA!!!
# CALCULADORA 2.0

num1 = float(input("Ingresa un número: "))
op = input("Ingresa un operador: ")
num2 = float(input("Ingresa otro número: "))

if op == "+":
    res = num1 + num2
    print("La suma es: " + str(res))
elif op == "-":
    res = num1 - num2
    print("La resta es: " + str(res))
elif op == "*":
    res = num1 * num2
    print("La multiplicación es: " + str(res))
else:
    print("El operador es invalido")

