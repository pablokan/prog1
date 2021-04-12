lista = ["uno", "dos", "tres"]
otraLista = ["cuatro", "cinco", "seis"]

print("next")
print(next(enumerate(lista)))

print("for")
for i,v in enumerate(lista, start=1):
    print(i, v)

print("zip")
for u, d in zip(lista, otraLista):
    print(u, d)

for i, (u, d) in enumerate(zip(lista, otraLista)):
    print(i, u, d)


