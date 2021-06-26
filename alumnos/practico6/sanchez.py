movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

gene=[]
title=[]
year=[]
def nomGenero():                # Construye una lista con los generos de los titulos
    for i in range(len(movies)):
        gen=movies[i].find(')')+1
        gene.append(movies[i][gen:])
        tit=movies[i].find('(')-1
        title.append(movies[i][:tit+1])
        year.append(int(movies[i][tit+2:gen-1]))
    return gene,title, year

genero, titulo, año = nomGenero()

consultaGenero=input('¿Qué genero quiere consultar? (Acción/Comedia/Ciencia Ficción) ')
estrenoAnio=int(input('¿Qué año de estreno busca? '))
inicial=input('¿Qué inicial de Título quiere localizar? ')

if consultaGenero=='Acción':
    print('Películas de ', (genre['act']))
    for n in range(0,len(movies)):
        if genero[n]=='act':
            print('- ', titulo[n])
elif consultaGenero=='Comedia':
    print('Películas de ', (genre['com']))
    for n in range(0,len(movies)):
        if genero[n]=='com':
            print('- ', titulo[n])
else:
    print('Películas de ', (genre['sf']))
    for n in range(0,len(movies)):
        if genero[n]=='sf':
            print('- ', titulo[n])            
print(year)   
for n in range(len(year)):
    print(estrenoAnio, type(estrenoAnio))
    if estrenoAnio < year[n]:
        print(titulo[n],' Año:', year[n], ' Género:', (genre[gene[n]]))

for m in range(len(titulo)):
    if inicial==titulo[m][0]:
        print(titulo[m],' Año:', year[m], ' Género:', (genre[gene[m]]))