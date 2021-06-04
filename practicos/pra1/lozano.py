nom = ["Ana Torres","Kate Hudson","Benicio Quesada","Susana Campoamores","Carlos Santamaria","Azul Skarsgard","Walter Catalejos"]
nac = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
sexo = ["f","f","m","f","m","f","m"]
sacar = ["na","ate","enicio","usana","arlos","zul","alter"]
a = (nom[0].split(sacar[0]))
b = (nom[1].split(sacar[1]))
c = (nom[2].split(sacar[2])) 
d = (nom[2].split(sacar[2])) 
e = (nom[4].split(sacar[4])) 
f = (nom[5].split(sacar[5])) 
g = (nom[6].split(sacar[6]))
t = ['  ']
fii = a + t + b + t + c + t + d + t + e + t + f + t + g 

fi = ''
for x in range (len(fii)):
    if fii[x] != '""':
        fi = fi + fii[x]
fo = fi.split('  ')
for i  in fo:
    if i == '  ':
        fio = fo.insert('.',1)
print(fio)