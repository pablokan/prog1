nom = ["Ana Torres","Kate Hudson","Benicio Quesada","Susana Campoamores","Carlos Santamaria","Azul Skarsgard","Walter Catalejos"]
nac = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
sexo = ["f","f","m","f","m","f","m"]
sacar = ["na","ate","enicio","usana","arlos","zul","alter"]
a = (nom[0].split(sacar[0]))
b = (nom[1].split(sacar[1]))
c = (nom[2].split(sacar[2])) 
d = (nom[3].split(sacar[3])) 
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
agg = '. '
foa = ','.join(fo)
foi = foa.replace(' ',agg)
foii = foi.split(',')
print('1)')
print('Iniciales y apellido de las personas:')
for i in range(len(foii)):
    print(foii[i])

###################################### PRIMERA PARTE ############################################

def encontrar_la_palabra_mas_larga(palabras):
    pal_long = []
    for p in palabras:
        pal_long.append((len(p),p))
    pal_long.sort()
    return pal_long[-1][1]
palabras = ['Ana','Kate','Benicio','Susana','Carlos','Azul','Walter']
print('2)')
print('El nombre mas largo es: ',encontrar_la_palabra_mas_larga(palabras))

###################################### SEGUNDA PARTE ############################################
print('3)')
from calcula_edad import edad

def personas():
    nac = '02/05/1943,07/09/1984,10/02/1971,21/12/1967,30/01/1982,30/08/1995,18/07/1959'
    naci = nac.replace('/','-')
    fecha = naci.split(',')
    sexo = ["f","f","m","f","m","f","m"]
    return fecha,sexo

fn, se = personas()
muj = 0
edadm = 0 
for i in range(len(se)):
    if se[i] == 'f':
        muj = muj + 1
        edadm = edadm + edad(fn[i]) 
prom = edadm / muj
prom = int(prom)



print('El promedio de edad de las mujeres es:',prom)
###################################### TERCERA PARTE ############################################