# BUSQUEDA BINARIA

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
lista.sort()
print(lista)

# 1ro. buscar el punto medio (puntero)
# 2do. comprobar si el punto medio es el valor que buscamos
# 3ro. si el número es menor al valor que buscamos aumentamos inicio 1 sobre el puntero
# 4to. si el numero es mayor al valor que buscamos disminuimos el final 1 bajo el puntero
# 5to. si inicio mayor o igual que final entonces el valor no se encuentra en la lista


def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None


def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El número {valor} no se encontró"
    else:
        return f"El número {valor} se encuentra en la posición {res_busqueda}"


print(buscar_valor(15))


# TAREA PARA ESTUDIANTE, Realizar las modificaciones al código
# para poder ingresar los valores directamente desde consola
# y agregar un ciclo infinito realizar todas las busquedasque queramos
# y poder terminar el ciclo.
