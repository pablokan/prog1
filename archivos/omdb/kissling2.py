class convertidor ():
    def __init__(self):
        pelis = open("omdb/pelis.json","r",encoding="utf8")
        c="tumama"
        self.texto=""
        while c != "":
            c = pelis.read(1)
            p = ""
            self.texto+=c
        pelis.close()

a=convertidor()
print (a.texto)
