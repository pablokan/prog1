class armarArchivo():
    def cabecera(self): #solo anota en el archivo txt los valores de la cabecera
        datos.write("Nombre, Actor, Rating, Recaudacion\n")

    def buscarValor(self,repeticiones,valorBuscado,posiDesplaz): #algoritmo generico para buscar un valor en pelis.json
        for i in range(repeticiones):
            c = " "
            while c != valorBuscado:
                c = peliculas.read(1)
                if c == valorBuscado:
                    peliculas.seek(peliculas.tell() + posiDesplaz)

    def armarPalabra(self,valorFinal): #algoritmo generico para armar una palabra
        palabra = ""
        m = " "
        while m != valorFinal:
            m = peliculas.read(1)
            if m != valorFinal:
                palabra +=  m    
        return palabra

    def titulo(self): # para buscar los titulos en el archivo pelis.json
        self.buscarValor(1,":",2)
        datos.write(self.armarPalabra('"') + ", ")

    def actorPrincipal(self): # para buscar actor principal de cada pelicula en el archivo pelis.json
        self.buscarValor(8,":",2)
        datos.write(self.armarPalabra(',') + ", ")

    def ratingRT(self): # para buscar el rating Rotten Tomatoes de cada pelicula en el archivo pelis.json
        self.buscarValor(11,":",2)
        datos.write(self.armarPalabra('%') + ", ")

    def recaudacion(self): # para buscar la recaudacion en el archivo pelis.json
        self.buscarValor(1,"$",0)
        recaudacion = self.armarPalabra('"')
        recaudacion2 = ""
        for i in range(len(recaudacion)):
            if recaudacion[i] != ",":
                recaudacion2 += recaudacion[i]
        datos.write(recaudacion2 + "\n")
        self.buscarValor(3,":",0) # con esto avanzamos hacia la otra pelicula en el archivo pelis.json

    def estructuraDatos(self): # define la estructura de escritura del archivo txt (sin la cabecera)
        pelicula = armarArchivo()
        pelicula.titulo()
        pelicula.actorPrincipal()
        pelicula.ratingRT()
        pelicula.recaudacion()

def promedio(): #funcion que obtiene el promedio
    prom = 0
    for e in lista:
        prom += int(e[2])
    prom = prom/len(lista)
    return prom

def recaudacionTotal(): #funcion que obtiene la suma total de las recaudaciones
    recTotal = 0
    for e in lista:
        recTotal += int(e[3])
    return recTotal    

peliculas = open("pelis.json", "r") #creacion del archivo txt
datos = open("datos.txt", "w")
pelis = armarArchivo()
pelis.cabecera()
for i in range(3):
    pelis.estructuraDatos()
peliculas.close()
datos.close()

datos = open("datos.txt", "r") #lectura del archivo txt para procesar sus datos
datos.readline()
lineas = datos.readlines()
lista = []
for li in lineas:
    lista.append(li.split(","))

opcion = ""
while opcion != "3": #menu para mostrar los datos
    print("\nSeleccione la opcion deseada:")
    print("1- obtener promedio del rating")
    print("2- obtener recaudacion total")
    print("3- Fin")
    opcion = input("\nOpción: ")
    if opcion == "1":
        print("el rating promedio es de:",promedio(),"%")
    elif opcion == "2":
        print("la recaudacion total es de $",recaudacionTotal())
print("Fin del programa")
datos.close()

















    

















                  




