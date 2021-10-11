class Mueble:
    def __init__(self, indicador, precio):
        self.indicador=indicador
        self.precio = precio
    
    def listarDatos(self):
        pass

class Silla(Mueble):
    def __init__(self, indicador, precio, tipo): #peso
        Mueble.__init__(self, indicador, precio)
        self.tipo = tipo
        #self.peso = peso

class Mesa(Mueble):
    def __init__(self, indicador, precio, forma): #personas
        Mueble.__init__(self, indicador, precio)
        self.forma = forma
        #self.personas = personas

class Banqueta(Mueble):
    def __init__(self, indicador, precio, tipo): #respaldo
        Mueble.__init__(self, indicador, precio)
        self.tipo = tipo
        #self.respaldo = respaldo

def agregarStock(lista):
    l=[]
    l=lista
    op=0
    seguir=True
    while seguir:
        while op != '4':
            print("¿Que mueble desea ingresar?")
            print('1- Mesa')
            print('2- Silla')
            print('3- Banqueta.')
            print('4- Salir')
            op = input()
            if op not in "1234":
                print ("ingrese una opcion valida")
                seguir=True
            elif op == '1':
                indicador="Mesa"
                print("Ingrese el precio de la Mesa.")
                precio=input()
                print("Ingrese la forma de la Mesa.")
                forma=input()
                mueble=Mesa(indicador,precio,forma)                    
            elif op == '2':
                indicador="Silla"
                print("Ingrese el precio de la Silla.")
                precio=input()
                print("Ingrese el tipo de silla.")
                tipo=input()
                mueble=Silla(indicador,precio,tipo)  
            elif op == '3':
                seguir=False
                indicador="Banqueta"
                print("Ingrese el precio de la Banqueta.")
                precio=input()
                print("Ingrese el tipo de Banqueta.")
                tipo=input()
                mueble=Banqueta(indicador,precio,tipo)
            else:
                seguir=False
        l.append(mueble)
        print("Desea seguir ingresando muebles al stock")
        print("1-Si")
        print("2-No")
        while op not in "12":
            if op not in "12":
                print ("ingrese una opcion valida")
                op=input()
            elif op=="1":
                seguir=True
            else:
                seguir=False
           
    return l


    
    
    

def menu():
    op = ''
    seguir=True
    while op != '4' or seguir:
        print('Que desea realizar?')
        print('1-Agregar muebles al stock')
        print('2- Consultar los artículos mayores a un precio solicitado.')
        print('3- Contar la cantidad de cada mueble discriminado por tipo.')
        print('4- Salir')
        op = input()
        if op not in "1234":
            print ("ingrese una opcion valida")
            seguir=True
        elif op == '1':
            
            agregarStock(l)
            
        elif op == '2':
            seguir=False
            masCaroQue(l,precio)
        elif op == '3':
            seguir=False
            contarPorTipo(l,mueble,tipo)
        else:
            seguir=False

    

def leerArchivo (nombre):
    l=[]
    f= open(nombre, "r")
    x = f.readlines() 
    for i in range(len(x)):
        l.append(x[i])
    f.close()
    return l
def escribirArchivo (nombre, lista):
    f=(open(nombre, "w"))
    for i in range(len(lista)):
        if i!=len(lista)-1:
            f.writelines(lista[i])
        else:
            f.writelines(lista[i])
    f.close()
l=[]
l2=[]
l=leerArchivo("stock_muebles.csv")
menu()
escribirArchivo("stock_muebles.csv",l)
