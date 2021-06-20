import csv
f = open('pelis.csv')
for row in csv.reader(f):
    print(row)
f.close()

""" 
# misma salida sin librería csv
g = open('pelis.csv')
for fila in g.readlines():
    print(fila[:-1].split(','))
g.close()
"""

f = open('pelis.csv')
for row in csv.DictReader(f):
    print(row)
f.close()




