from json import loads

def cleanNumber(s):
    n = ''
    for c in s:
        if c.isdigit():
            n += c
    return n

def buildCSVline(*args):
    line = ''
    for e in args:
        line += e + ','
    line = line[:-1] + '\n'
    return line

f = open('pelis.json', 'r')
a = f.read()
f.close()
d = loads(a)
f = open('pelis.csv', 'w')
f.write('Nombre,Actor,Rating,Recaudacion\n')
for e in d:
    title = e['Title']
    actor = e['Actors'].split(',')[0]
    rating = e['Ratings'][1]['Value'][:-1]
    caja = cleanNumber(e['BoxOffice'])
    f.write(buildCSVline(title, actor, rating, caja))
f.close()


