remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]
print('Faltantes:')
for x in range(len(remeras)): # Punto 1 
    for color, cantidad in remeras[x]['colores'].items():
        if cantidad == 0:
            print(remeras[x]['talle'], color)
colores = {}
for x in range(len(remeras)): # Punto 2
    for color, cantidad in remeras[x]['colores'].items(): 
        if color not in colores.keys():
            colores[color] = cantidad
        else:
            colores[color] += cantidad
print('Colores de remeras con menos unidades:', min(colores, key = colores.get))
print('Remeras con mayor stock por talle y color:')
max = 0
for x in range(len(remeras)): # Punto 3
    for color, cantidad in remeras[x]['colores'].items():
        if cantidad > max:
            max = cantidad
print('Cantidad:', max)
for x in range(len(remeras)):
    for color, cantidad in remeras[x]['colores'].items():
        if max == cantidad:
            print(remeras[x]['talle'], color)