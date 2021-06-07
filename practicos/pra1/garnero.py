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

def separarNombreyApellido(indice,nombApell,):
    separador = nombApell[indice].split(", ")
    nomb = separador[1]
    apell = separador[0]
    return nomb , apell

def invertirNombre(nomb , apell , invNomb):
    p_letra = nomb [0]
    l_apellido = p_letra + "." + apell
    invNomb.append(l_apellido)
    return invNomb

def palabra_larga(palabra):
    palabraLarga = []
    for p in palabra:
        palabraLarga.append((len(p),p))
    palabraLarga.sort()
    return palabraLarga[-1][1]    

def promedio(edadMujer):
    for e in edadMujer:
        p =sum(edadMujer)/len(edadMujer)
    return p


nombreApellido = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul","Catalejos, Walter"]
gen = ["f","f","m","f","m","f","m"]
nacim = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
cambio_nombre = []
nombres = []
edades= []
edadM = []
cont = 0


print('Iniciales y apellidos de las personas: ')
for x in range(len(nombreApellido)):
    nombre,apellido = separarNombreyApellido(x,nombreApellido,)
    invertirNombre(nombre,apellido,cambio_nombre)
    print(cambio_nombre[x])

for x in range(len(nombreApellido)):
    nombre,apellido = separarNombreyApellido(x,nombreApellido,)
    nombres.append(nombre)

print('El nombre mas largo es:' + (palabra_larga(nombres)))


for i in range(len(gen)):
    if gen[i] == "f":
        edades.append(nacim[i])
for i in range(len(edades)):
    edadM.append(edad(edades[i]))

print('El promedio de edad de las mujeres es: ', (int(promedio(edadM))))
