arc = open("pelis.json", "r")

def menu():
    op = ""
    while op != "4":
        print("\n¿Qué desea hacer?:")
        print("1- Obtener datos de películas")
        print("2- Obtener rating promedio")
        print("3- Obtener suma de recaudaciones")
        print("4- Fin")
        op = input("Opción: ")

        if op == "1":
            movies = open("pelis.txt","w")
            movies.write("Nombre, Actor, Rating, Recaudación \n")
            for i in range(3): #Pude haber creado un objeto y escribrir con los atributos
                count = 0      #Pero no lo vi necesario, ya que solo los utilizo en un módulo
                name = GetName()      #Y luego saco los datos del archivo de texto nuevo. 
                actors = GetActors()
                rating = GetRating()
                profit = GetProfit()
                while count < 1: 
                    n = arc.read(1)
                    if n == "}":
                        count = count+1 
                movies.write(str(name)+", "+str(actors)+", "+str(rating)+", "+str(profit)+"\n")
            movies.close()
            arc.close()
            print("Datos obtenidos!")            
        elif op == "2":
            RatingProm()
        elif op == "3":
            TotalProfit()
        elif op == "4": 
            print("Hasta luego!")

def GetName():
    i = "none"
    while i != "":
        n = arc.read(1)
        if n == "T": 
            arc.seek(arc.tell()+8)
            posi1 = arc.tell()
            break
    while i != "":
        n = arc.read(1)
        if n == ",":
            arc.seek(arc.tell()-2)
            posi2 = arc.tell()
            break
    arc.seek(posi1)
    title = arc.read(posi2-posi1)
    return title

def GetActors():
    i = "none"
    count = 0
    while count < 8: # Buscarà la cantidad de ":" que hay en el archivo hasta la palabra "Actors", cuando termine, saldrà de ahì y el cursor estarà al principio de la lista
        n = arc.read(1)
        if n == ":":
            arc.seek(arc.tell()+2)
            posi1 = arc.tell()
            count = count+1
    arc.seek(posi1)
    while i != "":
        n = arc.read(1)
        if n == ",": #El nombre del actor principal termina cuando se encuentra la primera coma dentro de la lista. 
            arc.seek(arc.tell()-1)
            posi2 = arc.tell()
            break
    arc.seek(posi1)
    actor = arc.read(posi2-posi1)
    return actor
def GetRating():
    i = "none"
    while i != "": 
        n = arc.read(1)
        if n == "%":
            arc.seek(arc.tell()-3)
            posi = arc.tell()
            break
    rating = arc.read((posi+2)-posi)
    return rating

def GetProfit():
    i = "none"
    while i != "": 
        n = arc.read(1)
        if n == "$":
            arc.seek(arc.tell())
            posi1 = arc.tell()
            break
    arc.seek(posi1)
    count = 0
    while count < 3: 
        n = arc.read(1)
        if n == ",":
            arc.seek(arc.tell())
            posi2 = arc.tell()
            count = count+1    
    arc.seek(posi1)
    n = arc.read((posi2-2)-posi1)
    profit = ""
    for i in n:
        if i != ",":
            profit = profit + i
    profit = int(profit)
    return profit

def RatingProm():
    movies = open("pelis.txt","r")
    acum = 0
    movies.seek(35) #Saltea el primer renglón
    for i in range(3):
        count = 0
        while count  < 2:
            n = movies.read(1)
            if n == "\n": #cuando llega al final de la linea, vuelve a empezar.
                count = 0
            if n == ",":
                movies.seek(movies.tell()) 
                posi = movies.tell()
                count = count + 1  
        movies.seek(posi)
        num = movies.read(posi-(posi-3))
        num = int(num)
        acum = acum+num
        prom = acum/3
    print("Promedio de ratings: ",prom)
    movies.close()

def TotalProfit():
    movies = open("pelis.txt","r")
    acum = 0
    movies.seek(37) #Saltea el primer renglón
    for i in range(3):
        count = 0
        while count  < 3:
            n = movies.read(1)
            if n == ",": 
                movies.seek(movies.tell())
                posi1 = movies.tell()
                count += 1 
        while n != "\n":
            n = movies.read(1)
        movies.seek(movies.tell()-1)
        posi2 = movies.tell()    
        movies.seek(posi1)
        num = movies.read((posi2-1)-posi1)
        num = int(num)
        acum = acum + num
    print("Total de recaudaciòn: ",acum)
    movies.close()
menu()