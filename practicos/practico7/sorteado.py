# paises = dict(sorted(paises.items(), key=lambda x: x[1], reverse=True))
# [key for key, val in dic.items() if val == value]

def cuadrado(x):
    return x*x
print(cuadrado(3))
print((lambda x: x*x)(3))
lista = [2, 1, 3, -4]
print(list(map(lambda x: x*x, lista)))
print(list(filter(lambda x: x>1, lista)))

def stringuea(x):
    return str(x)

print(list(map(lambda x: str(x), lista)))
print(list(map(stringuea, lista)))
print([str(x) for x in lista if x>1])

nuevaLista = []
for e in lista:
    nuevaLista.append(e*e)
print(nuevaLista)



