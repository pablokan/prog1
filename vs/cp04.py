# create a list of names
names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]

def inputMovies():
    '''ask the user to enter a list of movies, one pe line'''
    movies = []
    while True:
        movie = input("Enter a movie (or 'done'): ")
        if movie == "done":
            break
        movies.append(movie)
    return movies

    
    




