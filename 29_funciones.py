# FUNCIONES
# Una función es un bloque de código que incluye instrucciones para realizar
# una taréa específica


def saludar_usuario(par1, par2):
    print("Hola " + par2 + " tienes " + par1 + " años")
    print("Adios")


# print("primero")
# saludar_usuario("35", "Marcos")
# print("ultimo")

# FUNCIONES LAMBDA
# Son funciones anónimas que se ejecutan en una linea es decir solo pueden tener una expresión

resultado = lambda numero: numero + 20

suma = lambda numero1, numero2: numero1 + numero2

print(suma(30, 60))
