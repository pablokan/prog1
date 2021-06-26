from json import loads

f = open('practicos/practico7/practico7.json', 'r')
a = f.read()
f.close()
d = loads(a)

paises = []
for e in d:
    paises.append(e['location']['country'])
paises = dict.fromkeys(set(paises), 0)
for e in d:
    if e['location']['country'] in paises:
        paises[e['location']['country']] += 1
paises = dict(sorted(paises.items(), key=lambda x: x[1], reverse=True))
for k, v in paises.items():
    print(k, ":", v, 'personas')

from collections import Counter
lang = []
for e in d:
    lang.extend(e['languages'])
#print(lang)
d = dict(Counter(lang))
#print(d)
maxi = max(d.values())

def getKeys(dic, value):
    return [key for key, val in dic.items() if val == value]

print(maxi, 'personas hablan:')
for i in getKeys(d, maxi):
    print(i)







    
    
