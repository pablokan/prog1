# Dada la siguiente lista de diccionarios con datos de remeras, sus talles, colores y cantidades:

remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]

# Obtener:
# 1-Las faltantes, por talle y color.
# 2-El o los colores de remeras de menor cantidad.
# 3-Las remeras con mayor stock, por talle y color.


#ACTIVIDAD Nº1:

faltantes = []
colorMenorCantidad = []
for i in range(len(remeras)):
    tallesRemeras = remeras[i]['talle']
    cantidadRemeraRoja = remeras[i]['colores']['rojo']
    cantidadRemeraVerde = remeras[i]['colores']['verde']
    cantidadRemeraAzul = remeras[i]['colores']['azul']
    cantidadRemeraBlanco = remeras[i]['colores']['blanco']
    if cantidadRemeraRoja == 0:
        faltantes.append(remeras[i]['talle'])
    elif cantidadRemeraVerde == 0:
        faltantes.append(remeras[i]['talle'])
    elif cantidadRemeraAzul == 0:
        faltantes.append(remeras[i]['talle'])
    elif cantidadRemeraBlanco == 0:
        faltantes.append(remeras[i]['talle'])
        
        # if cantidadRemeraRoja >= cantidadRemeraVerde or cantidadRemeraRoja>=cantidadRemeraAzul or cantidadRemeraRoja>=cantidadRemeraBlanco:
        #     colorMenorCantidad.append(remeras[i]['colores'])
    
print(f'Remeras faltantes: {faltantes}')


#ACTIVIDAD Nº2:
