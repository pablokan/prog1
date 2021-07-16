# e = {"name":"Jacobo Coudray","location":{"country":"France","city":"Nog"}}
# print(e["location"]["country"])
# lista = []
# f = {"name":"Jacobo","languages":["Armenian","Indonesian"]}
# g = {"name":"Luis","languages":["English","French"]}
# lista.extend(f["languages"])
# lista.extend(g["languages"])
# print(lista)
from collections import Counter
lista = 'a a b c d c e a c a c z x m'.split()
q = dict(Counter(lista))
print(q)
maxi = max(q.values())
print(maxi)

