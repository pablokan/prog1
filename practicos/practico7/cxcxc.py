def getKeys(dic, value):
    return [key for key, val in dic.items() if val == value]

d = {'Francés': 5, 'Quechua': 9, "Danés": 3, "armenio": 9}
maxi = max(d.values())
print(maxi)

print(getKeys(d, maxi))

otraLista = []
for key, val in d.items():
    if val == 9:
        otraLista.append(key)
print(otraLista)

lista = [8,9,56]
print([elemento*2 for elemento in lista if elemento > 10])
