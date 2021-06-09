def menu():
    op = ""
    while op != "4":
        print("\nMenú de Opciones de analisis de peliculas y generar archovo .txt")
        print("1- Obtener datos de peliculas")
        print("2- Obtener rating promedio")
        print("3- Obtener suma de recaudaciones")
        print("4- Fin")
        op = input("Opción: ")

        if op == "1":
            nomb = input("Ingrese el nombre del archivo: ")
            cant = int(input("Ingrese el numero de peliculas a analizar: "))
            pel = open(nomb,"r")
            output_file = open("pelis.txt" , "w")
            output_file.write("Nombre, Actor, Rating, Recaudacion \n")
            for i in range (cant):
                c = 0
                name = getName(pel)
                actor = getActor(pel)
                rate = getRating(pel)
                profit = getProfit(pel)
                while c < 1:
                    n = pel.read(1)
                    if n == "}":
                        c = c+ 1  
                output_file.write(str(name)+", "+str(actor)+", "+str(rate)+", "+str(profit)+"\n")
            output_file.close()
            pel.close()     
        elif op == "2":
            rate = ratingProm()
            print("El rating promedio de las peliculas es ",rate)
        elif op == "3":
            suma = sumProfit()
            print("Total de recaudaciòn: ",suma)
        elif op == "4": 
            print("Gracias por utilizar nuestro software de analisis")

def getName(pel):
    p = "algo"
    while p != "":
        n = pel.read(1)
        if n == "T":
            pel.seek(pel.tell()+8)
            i = pel.tell()
            break
    while p != "":
        n = pel.read(1)
        if n == ",":
            pel.seek(pel.tell()-2)
            f = pel.tell()
            break
    pel.seek(i)
    title = pel.read(f-i)
    return title

def getActor(pel):
    c = 0
    p = "algo"
    while c < 8:
        n = pel.read(1)
        if n == ":":
            pel.seek(pel.tell()+2)
            i = pel.tell()
            c = c + 1
    pel.seek(i)
    while p != "":
        n = pel.read(1)
        if n == ",":
            pel.seek(pel.tell()-1)
            f = pel.tell()
            break
    pel.seek(i)
    actor = pel.read (f-i)
    return actor

def getRating(pel):
    p = "algo"
    while p != "":
        n = pel.read(1)
        if n == "%":
            pel.seek(pel.tell()-5)
            i = pel.tell()
            pel.seek(pel.tell()+2)
            f = pel.tell()
            break
    rating = pel.read(f-i)
    return rating

def getProfit(pel):
    c = 0
    p = "algo"
    while p != "":
        n = pel.read(1)
        if n == "$":
            i = pel.tell()
            break
    pel.seek(i)
    while c < 3:
        n = pel.read(1)
        if n == ",":
            pel.seek(pel.tell())
            f = pel.tell()
            c = c + 1
    pel.seek(i)
    profit = pel.read((f-2)-i)
    r = ""
    for i in profit:
        if i != ",":
            r = r + i
    profit = int(r)
    return profit

def ratingProm():
    data = open("pelis.txt","r")
    acum = 0
    data.seek(35) 
    for i in range(3):
        c = 0
        while c  < 2:
            n = data.read(1)
            if n == "\n": 
                c = 0
            if n == ",":
                data.seek(data.tell()) 
                pos = data.tell()
                c = c + 1
        data.seek(pos)
        num = int(data.read(pos-(pos-3)))
        acum = acum + num
    return (acum/3)
    data.close()

def sumProfit():
    data = open("pelis.txt","r")
    acum = 0
    data.seek(37) 
    for i in range(3):
        c = 0
        while c < 3:
            n = data.read(1)
            if n == ",": 
                data.seek(data.tell())
                posi1 = data.tell()
                c = c + 1 
        while n != "\n":
            n = data.read(1)
        data.seek(data.tell()-1)
        posi2 = data.tell()
        data.seek(posi1)
        num = data.read((posi2-1)-posi1)
        num = int(num)
        acum = acum + num
    return acum
    data.close()
menu()
