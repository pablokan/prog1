movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

nombres = []
moviesA = "".join(map(str, movies))  # converti la lista en string
print(moviesA)
""" 
for p in range(len(moviesA)):
    consulta = input('Ingrese el genero de peliculas que desea ver: \n act: Acción \n sf: Ciencia Ficción \n com: Comedia \n')
    consultaGenero = moviesA[p]
    posParentesis = consultaGenero.find(')')
    posGenero = consultaGenero.find('"')
    genero = consultaGenero[posParentesis:posGenero-1]
    
    if consulta == genero: 
        peli = moviesA[p]
        inicioNombrePeli = peli.find('"')
        finNombrePeli = peli.find('(')
        nombre = peli[inicioNombrePeli:finNombrePeli-1]
        print('Las peliculas del genero selecionado son:', nombre)
"""












# for i in range(len(nombresCompletos)):
#     nombreCompleto = nombresCompletos[i]
#     posComa = nombreCompleto.find(", ")
#     inicial = nombreCompleto[posComa + 2]
#     apellido = nombreCompleto[0:posComa]
#     nombre = nombreCompleto[posComa + 2:]
#     nombreCompleto = inicial + '. ' + apellido
#     print(nombreCompleto)
#     print('------------')
#     print(nombre)
#     print('------------')
