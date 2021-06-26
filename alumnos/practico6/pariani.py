movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

def f1(gen):
    for x in range(len(movies)):
        par = movies[x].find(gen)
        genero = movies[x][:par+1]
        print(genero)
        #return(genero)

busq = input("ingrese el genero que desea buscar (act,sf,com): ")
f1(busq)

# for d in genre:                 no capte como utilizar el diccionario en estos ejercicios
#     genre1 = (d[busq])
#     print(genre1)
#     print(genero)


def f2(año1):

    contador = 0

    for a in range(len(movies)):

        pare1 = movies[a].find("(")
        pare2 = movies[a].find(")")

        pelicula = movies[a][:pare1]

        añoM = movies[a][pare1+1:pare2]

        añoM = int(añoM)

        if añoM < año1:

            contador = contador + 1
        
    return contador



año = int(input("ingrese el año: "))

print("la cantidad de peliculas estrenadas antes de" , año , "son:" , f2(año))


def f3(letraBus):

    for l in range(len(movies)):         #este no se me ocurrio como hacerlo

        s = movies[l][:1]
        posiL = s[l].find(letraBus)


buscarletra = input("ingrese la letra para buscar la pelicula: ")
