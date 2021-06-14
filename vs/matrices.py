matriz = []
fila = [x for x in range(10)]

for x in range(10):
    fila = [n+1 for n in fila]
    matriz.append(fila)

print(matriz)

for f in matriz:
    print(f)
print('Posición 2,2: ', matriz[2][2])



        
