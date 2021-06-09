a = open("omdb/palabras.txt", "r")

c = " "

while c != "":
    c = a.read(1)
    if c!= "":
        z = str(ord(c)) + ":" + c
        print(z, end="/")

a.close()


