pelis = open("omdb/pelis.json", "r")
x = "x"
largo = ""
while x == "x":
    caracter = pelis.read(1)
    largo += caracter
    if caracter == ",":
        x = "y"
        print(largo[26:len(largo)-2])