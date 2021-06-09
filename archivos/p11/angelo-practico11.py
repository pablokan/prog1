# Barria Chavol Angelo - Practico Nro 11
class Operaciones ():

    def suma(self, lista):
        aux = 0
        for i in lista:
            aux += i
        return aux
    
    def promedio(self, lista):
        aux = self.suma(lista)
        aux = aux / len(lista)
        return aux

class App ():

    def __init__(self):
        op = 0
        while op != 3:
            print ("-----------------------------")
            print ("1- Cargar")
            print ("2- Mostrar Estadisticas")
            print ("3- Salir")
            op = int(input("Elija una opción (1 - 2 - 3)"))
            if op == 1:
                self.carga()
            elif op == 2:
                self.mostrar()
            elif op == 3:
                print("-----------------------------")
                print("Se ejecuto la opcion Salir")
                print("Gracias por usar este sistema")
                print("-----------------------------")
    
    def carga(self):
        json = open("prog1/practicos/pelis.json", "r")
        new = open("prog1/practicos/pelis.txt", "w")
        new.write("Nombre, Actor, Rating, Recaudacion\n")
        contador = 0
        c = "init"
        while c != '':
            c = json.read(1)
            if c == ":":
                contador += 1
                if contador == 1:
                    posi = json.tell()
                    titulo = self.busqueda(json,posi, '"')
                elif contador == 9:
                    posi = json.tell()
                    actorP = self.busqueda(json, posi, ",")
                elif contador == 20:
                    posi = json.tell()
                    rating = self.busqueda(json, posi, "%")
                elif contador == 29:
                    posi = (json.tell() + 1)
                    recaudacion = self.busqueda(json, posi, '"')
                    recaudacion = self.clean(recaudacion, ",")
                elif contador == 32:
                    new.write(titulo+ ", " + actorP+ ", " + rating +", " + recaudacion + "\n")
                    contador = 0
        new.close()
        json.close()
        print("-----------------------------")
        print("Se ejecuto la opcion Cargar")

    def mostrar (self):
        esta = Operaciones()
        archivo = open("prog1/practicos/pelis.txt", "r")
        listaRating = []
        listaRecaudacion = []
        encabezado = archivo.readline()
        lineas = archivo.readlines()
        for li in lineas:
            contador = 0
            aux = ""
            aux2 = ""
            for i in li:
                if i in ",":
                    contador += 1
                if contador == 2 and i not in " ,":
                    aux = aux + i
                if contador == 3 and i not in " ,":
                    aux2 = aux2 + i
            listaRating.append(int(aux))
            listaRecaudacion.append(int(aux2))
        print("-----------------------------")
        print("Se ejecuto la opcion Mostrar Estadisticas")
        print("El promedio de rating es de: ", esta.promedio(listaRating))
        print("La recaudacion total es de: $", esta.suma(listaRecaudacion))

    def busqueda (self, file, posicion, caracter):
        aux = ""
        c = ""
        file.seek(posicion + 2)
        while c != caracter:
            aux = aux + c
            c = file.read(1)
        return aux

    def clean (self, texto, caracter):
        aux = ""
        for i in texto:
            if i not in caracter:
                aux += i
        return aux

App()