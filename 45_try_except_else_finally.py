# TRATANDO CON ERRORES EN PYTHON
# try...except...else...finally

try:
    num1 = int(input("Ingresa un número: "))
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Entrada invalida, debe ser un entero")
else:
    print("No hubo ningun error")
finally:
    print("Se ejecuta siempre sin importar que pase")

# MEJORAR NUESTRA CALCULADORA 2.0 Y AÑADIRLE
# 1 - Tratamiento de errores posibles
# 2 - Ciclo infinito
