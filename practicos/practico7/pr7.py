from json import loads

f = open('practico7.json', 'r')
a = f.read()
f.close()
d = loads(a)

paises = {}
for e in d:
    pais = e['location']['country']
    if pais not in paises.keys():
        paises[pais] = 1
    else:
        paises[pais] += 1

paises = dict(sorted(paises.items(), key=lambda x: x[1], reverse=True))
print('Personas por país')
for k, v in paises.items():
    print(k, ":", v)

print()

from collections import Counter
lang = []
for e in d:
    lang.extend(e['languages'])
d = Counter(lang)
maxi = max(d.values())

def getKeys(dic, value):
    return [key for key, val in dic.items() if val == value]

print('Idiomas más hablados')
print(maxi, 'personas hablan:', end=' ')
idiomas = ''
for i in getKeys(d, maxi):
    idiomas += i + ', '
print(idiomas[:-2])







    
    
