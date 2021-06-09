# Angelo Barria Chavol - Practico N10
class App():
    def __init__(self):
        self.menu()

    def carga(self):
        lisDeuda = open ("pr10/deudores.txt", "r", encoding = "utf8")
        self.encabezado = lisDeuda.readline()
        self.todo = lisDeuda.readlines()
        self.a = len(self.todo)
        print ("Se leyeron:",self.a, "lineas")
        lisDeuda.close()

    def busqueda(self):
        archivo = open("morosos.txt",'w')
        cont = 0
        for li in self.todo:
            if "/2019" in li:
                aux = li.find("$")
                aux2 = li.find (".",aux)
                deuda = int(li[(aux+1):aux2])
                if  deuda >= 200000:
                    if cont == 0:
                        archivo.write("id, nombre, mail, deuda\n")
                    cont +=1
                    aux = li.find(",")
                    aux2 = li.find(",",aux+1)
                    nombre = li[(aux+1):aux2]
                    aux = li.find(",",aux2+1)
                    mail = li[(aux2+1):aux]
                    linea = str(cont) + ", " + nombre + ", " +mail + ", " + str(deuda) + "\n"
                    archivo.write(linea)
        archivo.close()

    def muestra(self):
        archivo = open("morosos.txt", "r")
        for li in archivo:
            li = li[:-1]
            print(li)
        archivo.close()
    
    def menu(self): 
        op = ""
        while op != "4":
            print ("_________________________")
            print("Menú de Opciones")
            print("1- Carga")
            print("2- Busqueda")
            print("3- Mostrar resultados")
            print("4- Salir")
            op = input("Opción: ")
            if op == "1":
                print ("_________________________")
                print("Carga")
                self.carga()
            elif op == "2":
                print ("_________________________")
                print("Busqueda")
                self.busqueda()
            elif op == "3":
                print ("_________________________")
                print("Mostrar resultados")
                self.muestra()
        print ("_________________________")
        print("Gracias, adios")

App()