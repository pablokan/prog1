# Cumplir: subprogramas (funciones x tarea), funciones (funciones x fragmento repetido)
# Operaciones sobre strings, listas, diccionarios
# archivos de texto (csv OR json?) OR both!
# 

remeras = [
    {'S': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
    {'M': {'rojo': 7, 'azul': 2, 'naranja': 7}},
    {'L': {'verde': 0, 'azul': 4}},
    {'XL': {'verde': 7, 'blanco': 6}}
]

# faltantes
for talles in remeras:
    for talle, colores in talles.items():
        for color, cantidad in colores.items():
            if cantidad == 0:
                print(talle, color)
        
    