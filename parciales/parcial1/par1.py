remeras = [
    {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
    {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
    {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
    {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]


cantidadXcolor = {'rojo': 0, 'verde': 0, 'azul': 0, 'blanco': 0}
mayorTalleyColor = []
mayor = 0
print('Faltantes: ', end='')
for tamanio in remeras:
    for color, cantidad in tamanio['colores'].items():
        # faltantes
        if cantidad == 0:
            salida = f"< {tamanio['talle']} {color} >"
            print(salida, end=' ')

        # acumulador de cantidad de remeras por color
        cantidadXcolor[color] += cantidad

        # número mayor x talle y color
        if cantidad >= mayor:
            mayor = cantidad
            mayorTalleyColor.append({'talle': tamanio['talle'], 'color': color, 'cantidad': cantidad})

print('\n\nColores de remeras con menos unidades: ', end='')
minimo = min(cantidadXcolor.values())
for color, cantidad in cantidadXcolor.items():
    if cantidad == minimo:
        print(color)

print('\nRemeras con mayor stock por talle y color:')
print('Cantidad:', mayor)
for d in mayorTalleyColor:
    if d['cantidad'] == mayor:
        print(d['talle'] + ' ' + d['color'])
    
