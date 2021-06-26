#########################
#####EZEQUIEL OLIVERO####
#########################

movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}


def genreSearch(movgenre):
    peliculas="Peliculas de "+movgenre+"\n"
    for objeto in movies:
        objeto=objeto+" "
        for parentesis in range(len(objeto)):
            if objeto[parentesis]=="(":
                pelicula=objeto[0:parentesis] #Das boot
                genero=genre[objeto[parentesis+6:-1]] #Accion
                if genero==movgenre:
                    peliculas=peliculas+pelicula+"\n"
    peliculas=peliculas[:-1]
    return(peliculas)
print(genreSearch("Acción"))     

def peliculasAño(año):        
    counter=0
    for objeto in movies:                                       
        for parentesis in range(len(objeto)):
            if objeto[parentesis]=="(":
                añoEstreno=objeto[parentesis+1:parentesis+5]
        if int(añoEstreno)<año:
            counter+=1
    return("Cantidad de estrenadas antes del año "+str(año)+": "+str(counter))
print(peliculasAño(1990))    

def movInfoSrch(letra):
    letra=letra.upper()
    movInfo="Películas cuyo nombre empieza con la letra "+letra+":\n"        
    for objeto in movies:
        objeto=objeto+" "
        for parentesis in range(len(objeto)-1,0,-1):
            if objeto[parentesis]=="(":
                pelicula=objeto[0:parentesis] 
                genero=genre[objeto[parentesis+6:-1]] 
                añoEstreno=objeto[parentesis+1:parentesis+5] 
                if pelicula[0]==letra:
                    movInfo=movInfo+pelicula+". Año: "+añoEstreno+". Género: "+genero+"\n"
    movInfo=movInfo[:-1]
    return movInfo
print(movInfoSrch("t"))

    
    