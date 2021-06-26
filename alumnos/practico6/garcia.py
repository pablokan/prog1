movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
          "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
          "Three Kings(1999)act", "The green hornet(2011)com"
          ]
genres = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}


def nameInputGenere(array, listMovies, genere):
    for value in listMovies.items():
        if value[0] == genere:
            films = ['Peliculas de '+value[1]]
    for i in array:
        if i[-3:] == genere or i[-2:] == genere:
            films.append('-'+str(i.split('(')[0]))
    return films


def filmsYear(array, year):
    filmseErlear = 0
    for i in array:
        if year > int(i.split('(')[1].split(')')[0]):
            filmseErlear += 1
    return filmseErlear


def firstLetter(array, letter):
    films = []
    elmts = []
    for i in array:
        if letter == i[0]:
            films.append(i)
    for j in films:
        filmName = j.split('(')[0]
        year = j.split('(')[1].split(')')[0]
        if j[-3:] == 'act' or j[-3:] == 'com':
            gen = genres[j[-3:]]
        elif j[-2:] == 'sf':
            gen = genres[j[-2:]]
        elmts.append([filmName, year, gen])
    print('Películas cuyo nombre empieza con la letra "', letter, '"')
    for k in elmts:
        print(k[0], '.', ' Año:', k
              [1], '.', 'Género: ', k[2])


ejercicio1 = nameInputGenere(
    movies, genres, input('Input a genere: (act/sf/com) '))
for i in ejercicio1:
    print(i) 

year = int(input('Input a year please: '))
ejercicio2 = 'Cantidad de estrenadas antes del año ' + \
    str(year)+':'+str(filmsYear(movies, year))
print(ejercicio2)

ejercicio3 = firstLetter(movies, 'D')

