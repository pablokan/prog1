
from datetime import date


def separeNameFormalName(fullNames):
    formalNames = []
    names = []
    for fullName in fullNames:
        array = fullName.split(', ')
        formalNames.append(array[1][0]+'. '+array[0])
        names.append(array[1])
    return formalNames, names


def nameMoreLonger(names):
    total = 0
    for name in names:
        if len(name) > total:
            total = len(name)
            nameLonger = name
    return nameLonger


def edad(fn):
    hoy = date.today()
    dn, mn, an = fn.split('-')
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


def averageWomanAge(datesOfBitrh, generes):
    total = 0
    divisor = 0
    for i in range(len(generes)):
        if generes[i] == 'f':
            total += edad(datesOfBirth[i])
            divisor += 1
    return int(total/divisor)


# Datos
fullNames = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana',
             'Santamaría, Carlos',  'Skarsgard, Azul',  'Catalejos, Walter']
generes = ['f', 'f', 'm', 'f', 'm', 'f', 'm']
datesOfBirth = ['02/05/1943', '07/09/1984', '10/02/1971',
                '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']
# Ejercicio 1

namesAndFormalNames = separeNameFormalName(fullNames)
names = namesAndFormalNames[1]
formalNames = namesAndFormalNames[0]

for formalName in formalNames:
    print(formalName)
# Ejercicio 2
print('El nombre más largo es:', nameMoreLonger(names))
# Ejercicio 3
for i in range(len(datesOfBirth)):
    datesOfBirth[i] = datesOfBirth[i].replace('/', '-')
print('El promedio de edad de las mujeres es:',
      averageWomanAge(datesOfBirth, generes))
