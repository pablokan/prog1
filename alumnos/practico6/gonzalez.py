movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}
aux= ""
def SegunGenero (genero,nombres): 
    for x in range(len(movies)):
        if genero == 1 and movies[x][-3:] == "act":
            if nombres == "":  
                aux = movies[x] 
                nombres = aux[:-9]
            else:
                aux = movies[x] 
                nombres = nombres + ", " + aux[:-9]
        elif genero == 2 and movies [x][-2:] == "sf":
            if nombres == "":
                aux = movies[x]
                nombres = aux[:-8]
            else:
                aux = movies[x]
                nombres = nombres + ", " + aux[:-8]
        elif genero == 3 and movies[x][-3:] == "com": 
            if nombres == "":
                aux = movies[x] 
                nombres = aux[:-9]
            else:
                aux = movies[x]
                nombres = nombres + ", " + aux[:-9]
    print("Las peliculas con el genero ingresado son: ",nombres)
def SegunAño (año):
    lista = 0
    for x in range(len(movies)):
        valor = movies[x].find("(")
        evaluar = 0
        evaluar = int(movies[x][valor+1:valor+5])
        if evaluar < año:
            lista = lista + 1
    print("La cantidad de pelculas estrenadas antes del año ",año,": ", lista)        
def SegunLetra (letra):
    print("Peliculas vuyo nombre empiezan con la letra *",letra, "*: ")
    for x in range(len(movies)):
        aux = ""
        generos = ""
        años = ""
        valor = movies[x].find("(")
        if letra == movies[x][0]:
            años = movies[x][valor+1:valor+5]
            parentesis = movies[x].find(")")
            if movies[x][parentesis+1:] == "act":
                generos = "Accion"
            elif movies[x][parentesis+1:] == "sf":
                generos = "Ciencia Ficcion"
            elif movies[x][parentesis+1:] == "com":
                generos = "Comedia"
            aux = movies[x][:valor-1] + ". Año: " + años + ". Genero: " + generos
            print(aux)

            
        

genero = int (input("Ingrese genero de la pelicula de la siguiente manera 1: Accion, 2 : Ciencia Ficcion, 3: Comedia : "))
SegunGenero(genero,aux)
año = int (input("Ingrese el año deseado: "))
SegunAño(año)
letra = input("Ingrese la letra deseada en mayuscula: ")
SegunLetra(letra)