# SENTENCIAS BREAK Y CONTINUE
# Las sentencias break y continue nos permiten manejar el flujo
# de la información en un bucle.

dias = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
]

for dia in dias:
    if dia == "jueves":
        break
    print(dia)