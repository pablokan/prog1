numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]
for n, e in zip(numeros, espanol):
    print(n, e)

zipeado = zip(numeros, espanol)
print(list(zipeado))

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)
