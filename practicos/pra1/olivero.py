nombres=["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul","Catalejos, Walter"]
f=["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
s=["f","f","m","f","m","f","m"]

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

##########################################################

def inicial_y_apellido(lista): #1)FUNCION REUTILIZABLE TERMINADA.
    for e in lista:    
        nombre=""
        for x in e:
                if x!=",":
                    nombre=nombre+x   
        nombreLista=nombre.split()  
        for x in nombreLista[1:]:
                for e in x:
                    inicialNombre=x[0] 
        resFinal=inicialNombre+". "+nombreLista[0]
        print(resFinal)

inicial_y_apellido(nombres)

##########################################################

def nombreMasLargo(lista):  #2)FUNCION REUTILIZABLE TERMINADA.  
    counterFin=0
    counter=0
    largestName=""
    counterName=""
    for e in lista:    
        nombre=""
        for x in e:
            if x!=",":
                nombre=nombre+x 
        nombreListaCompleto=nombre.split() 
        nombreLista=nombreListaCompleto[1]+" " 
        for t in nombreLista:
            if t!=" ":
                counter+=1    
                counterName+=t            
            else:          
                if counter>=counterFin:               
                    counterFin=counter                
                    largestName=counterName               
                counter=0
                counterName=""
    return("El nombre mas largo es "+largestName+" y tiene un largo de "+str(counterFin)+" caracteres.")

print(nombreMasLargo(nombres))

##########################################################

def promedioEdadesF(fechas,sexos):   #3) FUNCION REUTILIZABLE TERMINADA.
    numeroF=0
    sumaEdades=0 
    for x in range (len(sexos)):
        if sexos[x]=="f":   
            numeroF=numeroF+1     
            sumaEdades=sumaEdades+(edad(fechas[x]))
    promedioFin=sumaEdades/numeroF
    return promedioFin
print(promedioEdadesF(f,s)) 


