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

def nombreApellido (indice,nombresCompleto,): 
    separacion = nombresCompleto[indice].split(", ")
    nom = separacion[1]
    ape = separacion[0]
    return nom,ape

def cambioNom (nom,ape,cambioNombre):
    inicial = nom[0]
    iniApe = inicial + "." + ape
    cambioNombre.append(iniApe)
    return cambioNombre


nombre_completo = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul","Catalejos, Walter"]
genero = ["f","f","m","f","m","f","m"]
nacimiento = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
cambio_nombre = []
nombres = []
nombre = ""
apellido = ""
nombre_mayor = ""
nacimientoMujeres = []
edadMujeres = []
operador = 0

print("Iniciales y apellido de las personas: ")
for i in range(len(nombre_completo)):
    nombre,apellido = nombreApellido(i,nombre_completo,) # manda la lista completa en cada iteración
    cambioNom(nombre,apellido,cambio_nombre) 
    print(cambio_nombre[i])

for i in range(len(nombre_completo)):
    nombre,apellido = nombreApellido(i,nombre_completo,)
    nombres.append(nombre)
for i in range(len(nombres)):
    nombre = nombres[i]
    if len(nombre) > len(nombre_mayor):
        nombre_mayor = nombre
print("El nombre más largo es: ",nombre_mayor)

for i in range(len(genero)):
    if genero[i] == "f":
        nacimientoMujeres.append(nacimiento[i])
for i in range(len(nacimientoMujeres)):
    edadMujeres.append(edad(nacimientoMujeres[i]))
for i in range(len(edadMujeres)):
    operador = operador + edadMujeres[i]
promedio = operador / len(edadMujeres)
print("El promedio de edad de las mujeres es: ",promedio)
