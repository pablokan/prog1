
class Convertidor ():
    def __init__(self):
        pelis = open("p11/pelis.json","r",encoding="utf8")
        c="tumama"
        self.texto=""
        while c != "":
            c = pelis.read(1)
            p = ""
            self.texto+=c
        pelis.close()

    def Transformar(self,txt):
        self.lista=txt.split(" ")


class Nombre():
    def __init__(self):
        self.film =[]
    def buscador(self,lista,nom):
        for i in range (len(lista)):
            x=lista[i].find(nom)
            if x>0:
                self.film.append(lista[i+1])

class Menu ():
    A=Convertidor()
    A.Transformar(A.texto)
    B=Nombre()
    B.buscador(A.lista,"Title")
    C=Nombre()
    C.buscador(A.lista,"Actors")
    D=Nombre()
    D.buscador(A.lista,"Metascore")
    E=Nombre()
    E.buscador(A.lista,"BoxOffice")
    print ("Bienvenido")
    print ("Que pelicula eligira para brindarle informacion: ")
    print("1-Arrival ","2-Transcendence","3-Serenity")
    x=int(input("respuesta: "))
    for i in range (x):
        print ("eligio",B.film[x-1])
    
    print("Que informacion desea conocer?: ")
    print ("1-Actor principal ,2- Puntaje Promedio, 3- Cantidad recaudada")
    z=input("Respuesta: ")
    if z==1:
        print(C.film[0])
    elif z==2:
        print(D.film(1))
    elif z==3:
        print (E.film[2])