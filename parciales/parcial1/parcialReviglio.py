talles=[]
coloresPorTalle=[]
minimo=99999
c=0
color=''
mayor=0
mayorStock=''

remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]
colores=['rojo','verde','azul','blanco']

for e in remeras:
    talles.append(e['talle'])
for e in remeras:
    coloresPorTalle.append(e['colores'])

for a in range(len(talles)):
    for i in range(len(colores)):
        if (coloresPorTalle[a][colores[i]])==0:
            print(talles[a],colores[i])
                
for e in colores:
    for i in range(0,4):
        c=c+(coloresPorTalle[i][e])
    if c<minimo:
            minimo=c
            color=e
            c=0
print('Colores con menos unidades:',color)

for a in range(len(talles)):
    for e in colores:
        for i in range(0,4):
            if (coloresPorTalle[i][e])>mayor:
                mayor=(coloresPorTalle[i][e])

#hasta aca lleguè... demasiado