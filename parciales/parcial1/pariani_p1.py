remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 0, 'azul': 5, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]
diccF = {"talle" : [], "color": []}

list = []

for x in remeras:

    if x["colores"]["verde"] == 0:
        diccF["talle"] = x["talle"]
        diccF["color"] = "verde"

        list.append(diccF.copy())

    elif x["colores"]["rojo"] == 0:
        diccF["talle"] = x["talle"]
        diccF["color"] = "rojo"

        list.append(diccF.copy())
        
    elif x["colores"]["azul"] == 0:
        diccF["talle"] = x["talle"]
        diccF["color"] = "azul"

        list.append(diccF.copy())

    elif x["colores"]["blanco"] == 0:
        diccF["talle"] = x["talle"]
        diccF["color"] = "blanco"

print("faltantes: ")
print(list)

contadorRED = 0
contadorGreen = 0
contadorBlue = 0
contadorWhite = 0

listaMnores = []
listaColores = []

for c in remeras:

    contadorRED = contadorRED + c["colores"]["rojo"]
    contadorGreen = contadorGreen + c["colores"]["verde"]
    contadorBlue = contadorBlue + c["colores"]["azul"]
    contadorWhite = contadorWhite + c["colores"]["blanco"]


if contadorGreen < contadorBlue and contadorRED and contadorWhite:   #funciona para un caso
    print("el color con menos unidades es el verde: ", contadorGreen)


import operator
for x in remeras:

    BiggestKey = max(x["colores"].items(), key=operator.itemgetter(1))[0]

    print(x["talle"], " " , BiggestKey)