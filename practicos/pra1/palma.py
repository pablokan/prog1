nombrescompletos=["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana ","Santamaría, Carlos ","Skarsgard, Azul ","Catalejos, Walter "]
sexo=["f","f","m","f","m","f","m"]
fechasdenacimento=["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]  

nombrestextos=" ".join(nombrescompletos)

def f1(texto):
    s=""
    for e in texto:
        if e not in ",":
            s+=e
    return s.split()
textolista=f1(nombrestextos)

nombres = textolista[1::2]
apellidos=textolista[0::2]

inicialesnombres = ""
i=0
for p in nombres:
    inicialesnombres = inicialesnombres + p[0]+"."+ str(apellidos[i])+"\n"
    i+=1
print(inicialesnombres)

def f2(lista):
    posicion=0
    palabramaslarga=0
    i=0
    for i in range(len(lista)):
        if len(lista[i])>palabramaslarga:
            palabramaslarga=len(lista[i])
            posicion=i
    return(lista[posicion])
print("El nombre de pila mas largo es:", f2(nombres))

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
if __name__ == '__main__':
    suma=0
    contador=0
    for i in range(len(sexo)):
        if sexo[i]=="f":
            suma+=int(edad(fechasdenacimento[i]))
            contador+=1
promedio=int((suma)/contador)  
print("El promedio de edad de las mujeres es:",promedio)