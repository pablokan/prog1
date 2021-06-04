nombres_completos = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
sexos = ['f', 'f', 'm', 'f', 'm', 'f', 'm']
fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']

####################################################################################
#1)Mostrar las iniciales de los nombres con apellido completo de todas las personas.
####################################################################################
print('1) Iniciales y apellido de las personas:')
for i in nombres_completos:
    posi = i.find(' ')
    if posi != -1:
        posi = posi + 1
    nomc = i[0:posi+1]    
    nomc1 = nomc.split(', ')
    nomc1.reverse()
    nomf = '. '.join(nomc1)
    print(nomf)
####################################################################################
#2)Decir cual es el nombre de pila más largo.
####################################################################################
nombres = []
for x in nombres_completos:
    p = x.find(',')
    if p != -1:
        p = p + 2
    nombre = x[p:]
    nombres.append(nombre)

c = 0
for n in nombres:
    if len(n) > c:
        c = len(n)
        nml = n
print('2) El nombre más largo es:', nml)
####################################################################################
#3)Mostrar el promedio de edad de las mujeres.
####################################################################################
fechas_mujeres = []
for s in range(len(sexos)):
    if sexos[s] == 'f':
        fechas_mujeres.append(fechas[s])

from datetime import date
def edad(fn):
    hoy = date.today()
    dn, mn, an = fn.split('/')
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -= 1
    return e

prom = 0
for fm in range(len(fechas_mujeres)):
    em = edad(fechas_mujeres[fm])
    prom = prom+em

resultado = prom/4
print('3) El promedio de edad de las mujeres es:', int(resultado))