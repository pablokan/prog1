def getListOfTitles():
    """Ask the user to enter a list of books, one per line"""
    titles = []
    while True:
        title = input("Enter a book title: ")
        if title == "":
            break
        titles.append(title)
    return titles

def buildDictionaryOfCities():
    """Reads a file and builds a dictionary that maps from the name of a city to
    its country"""
    inFile = open("cities.txt", "r")
    cityToCountry = {}
    for line in inFile:
        line = line.strip()
        words = line.split(",")
        city = words[0]
        country = words[1]
        cityToCountry[city] = country
    inFile.close()
    return cityToCountry

def pickPrimaryColor():
    """Asks the user to enter a primary color"""
    while True:
        color = input("Enter a primary color: ")
        if color == "":
            break
        color = color.lower()
        if color == "red" or color == "blue" or color == "green":
            return color
        else:
            print("That is not a primary color")

def pickRandomColor():
    """Returns a random color by name"""


def listOfRandomColors():
    """Returns a list of 10 random colors"""
    import random
    colors = []
    for i in range(10):
        color = pickRandomColor()
        colors.append(color)
    return colors

def preguntarAlUsuarioPorUnaListaDeLibros():
    """Asks the user to enter a list of books, one per line"""
    books = []
    while True:
        title = input("Enter a book title: ")
        if title == "":
            break
        books.append(title)
    return books


def askListofMovies():
    """Asks the user to enter a list of movies, one per line"""
    movies = []
    while True:
        movie = input("Enter a movie title: ")
        if movie == "":
            break
        movies.append(movie)
    return movies

def askForMovies():
    """Asks the user to enter a list of 10 movies, one per line"""
    movies = []
    while True:
        movie = input("Enter a movie title: ")
        if movie == "":
            break
        movies.append(movie)
    return movies

def inputPrimaryColor():
    """Asks the user to enter a primary color"""
    while True:
        color = input("Enter a primary color: ")
        if color == "":
            break
        color = color.lower()
        if color == "red" or color == "blue" or color == "green":
            return color
        else:
            print("That is not a primary color")

color = inputPrimaryColor()
print(color)

def buildRandomListOfFloats():
    """Builds and returns a list of 10 random floats from -1 to 1"""
    randomList = []
    for i in range(10):
        randomList.append(random.random())
    return randomList

# create a list of names and print it
names = ["Alfred", "Bertrand", "Candace", "Dolores", "Eugenia", "Freda", "Greta", "Heidi", "Irene", "Juanita", "Karen", "Lorraine"]
print(names)

# create a list of random numbers and print it
randomList = buildRandomListOfFloats()







    









