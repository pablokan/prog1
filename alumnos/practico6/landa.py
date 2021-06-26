movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {
         'act': 'Acción', 
         'sf': 'Ciencia Ficción', 
         'com': 'Comedia'
}

def solicitarGenero (dGenero):
    gen= input("escriba el genero que corresponda(Acción/Ciencia Ficción/Comedia): ")
    for elementos in dGenero.items():
         if elementos[1] == gen:
             clave = elementos[0]
    return clave,gen

def evaluarGenero (gener0,peliculas,genCorto):
    print("Películas de",gener0)
    for i in peliculas:
        eva = i.find(genCorto)
        if eva != -1:
            posicionCorchete = i.find("(")
            print("-",i[:posicionCorchete])

def punto1 (lMovies,dGenre):
    generoCorto,generoLargo = solicitarGenero(dGenre)
    evaluarGenero(generoLargo,lMovies,generoCorto)

def punto2(peliculas):
    ano = int(input("introdusca el año de la pelicula: "))
    contador = 0
    for i in peliculas:        
        if ano >  int(i[i.find("(")+1:i.find(")")]):
            contador += 1
    print("Cantidad de estrenadas antes del año",ano,": ",contador)

def punto3(peliculas,generos):
    lpeliculas = []
    lanos = []
    lgeneros = []
    for pelicula in peliculas:
        m = pelicula.split("(")
        n = m[1].split(")")
        lpeliculas.append(m[0])
        lanos.append(n[0])
        lgeneros.append(n[1])
    letra = input("introdusca la letra con la que empieza la pelicula: ").upper()
    for i in range(len(lpeliculas)):
        if lpeliculas[i][0] == letra:
            print(lpeliculas[i],".Año:",lanos[i],".Genero:",generos[lgeneros[i]])

punto1(movies,genre)
punto2(movies)
punto3(movies,genre)
