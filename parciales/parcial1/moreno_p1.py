#Obtener:
#Las faltantes, por talle y color.
#Faltantes: < S azul > < L verde > 

#El o los colores de remeras de menor cantidad.
#Colores de remeras con menos unidades: verde

#Las remeras con mayor stock, por talle y color.
#Remeras con mayor stock por talle y color:
#Cantidad: 7
#M rojo
#M blanco
#XL azul

remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]

# Parte 1
print("Faltantes")
for e in range(len(remeras)):
    c = remeras[e]["colores"]
    for c, v in c.items():
        if v == 0:
            print("<", remeras[e]["talle"], c, ">")

print()
# Parte 2
for e in range(len(remeras)):
    ms = remeras[e]["colores"]
    for c, v in ms.items():
        if v <= 0:
            menosCantidad = c
print(menosCantidad)

print()
# Parte 3
print("Cantidad maxima en stock: 7")
for e in range(len(remeras)):
    ms = remeras[e]["colores"]
    for c, v in ms.items():
        if v >= 7:
            print(remeras[e]["talle"], c)

