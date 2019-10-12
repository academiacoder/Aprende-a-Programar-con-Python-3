from utilidades_extra import tirar_dado
# JUEGO DE POKEMON


# Creamos la clase Pokemon
class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def gano(self):
        print(f"{self.nombre} GANO ESTA BATALLA!!!")
        print("Más suerte la próxima vez!!!")


# Creamos nuestros pokemon
p1 = Pokemon("Pikachu", 60)
p2 = Pokemon("Bulbasur", 55)

# Inicializamos los valores y el turno
p1.vida = 100
p2.vida = 100
turno = tirar_dado(2)

print("HA INICIADO LA BATLLA")
print(f"{p1.nombre} se enfreta a {p2.nombre}\n")

while p1.vida > 0 and p2.vida > 0:
    if turno == 1:
        p2.vida = p2.vida - p1.ataque
        turno = 2
        print(f"{p1.nombre} ataca, {p2.nombre} ahora tiene {p2.vida} de vida")
        print("\n=== PRÓXIMA RONDA ===")
    else:
        p1.vida = p1.vida - p2.ataque
        turno = 1
        print(f"{p2.nombre} ataca, {p1.nombre} ahora tiene {p1.vida} de vida")
        print("\n=== PRÓXIMA RONDA ===")

# Consultamos si el pokemon 1 perdio
if p1.vida <= 0:
    p2.gano()
else:  # Sino significa que el pokemon 1 gano
    p1.gano()

# TAREA PARA EL ESTUDIANTE
# 1 Agregar un ciclo infinito que nos permita iniciar más batallas
# 2 Agregar más pokemons y permitir al usuario elegir cual utilizar
# 3 No pueden usar el mismo pokemon los 2 jugadores
# 4 casi opcional, sería ideal que la clase pokemon estuviera en un modulo
# aparte específico.
# Opcional:
# Agregar clases a los pokemon (Tierra, Electridad, Fuego, Agua)
# y darle a cada clase superioridad ante otras clases.
# por ejemplo, si pokemon 1 es de agua, y pokemon 2 es de fuego
# que el pokemon 1 le reste ataque * 1.5
# así mismo que el pokemon 2 le reste solo ataque menos el 25%


