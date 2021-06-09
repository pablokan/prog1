peliculas = open("omdb/pelis.json", "r")

c = " "
titulo = ""

while c != "T":
    c = peliculas.read(1)
    if c == "T":
        peliculas.seek(peliculas.tell() + 8)
        m = " "
        while m != '"':
            m = peliculas.read(1)
            if m != '"':
                titulo +=  m
print(titulo)   