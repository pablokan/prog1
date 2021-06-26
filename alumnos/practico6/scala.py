movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

def s():
    print('===============================================')

def consignaUno(genero):
    for m in range(len(movies)):
        posGenero = movies[m].find(genero)
        if posGenero != -1:
            f = movies[m].find('(')
            pelicula = movies[m][:f]
            print('- '+pelicula)
    
def consignaDos(año):
    c = 0
    for a in range(len(movies)):
        posParentesis = movies[a].find('(')
        if posParentesis != -1:
            f = movies[a].find(')')
            añoEstreno = int(movies[a][posParentesis+1:f])
            if int(año) > añoEstreno:
                c = c + 1
    return c

def consignaTres(letra):
    l = letra.upper()
    for i in range(len(movies)):
        posLetra = movies[i].find(l,0,1)
        if posLetra != -1:
            posParenAbierto = movies[i].find('(')
            posParenCerrado = movies[i].find(')')
            año = movies[i][posParenAbierto+1:posParenCerrado]
            peli = movies[i][:posParenAbierto]  
            gen =  movies[i][posParenCerrado+1:]
            print(peli+'.', 'Año:'+año+'.', 'Género:', genre[gen])

g = input('Ingrese un género (act:"Acción", sf:"Ciencia Ficción", com:"Comedia"): ')
a = input('Ingrese un año: ')
l = input('Ingrese una letra: ')

s()
print('Películas de', genre[g])
consignaUno(g)
s()
print('Cantidad de estrenadas antes del año', a+':', consignaDos(a))
s()
print('Películas cuyo nombre empieza con la letra', '"'+l.upper()+'":')
consignaTres(l)
s()