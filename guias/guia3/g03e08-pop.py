numeros = [1,2,3,4,5,6,7]

for i in range (len(numeros)):
    numeros.insert(i, numeros.pop())

print(numeros)
