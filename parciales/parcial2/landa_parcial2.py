class ProductoDeMadera():
    def __init__(self,mueble,tipo,precio):
        self.mueble = mueble
        self.tipo = tipo
        self.precio = precio

class Silla(ProductoDeMadera):
    def __init__(self,mueble,tipo,precio,peso):
        ProductoDeMadera.__init__(self,mueble,tipo,precio)
        self.peso = peso

class Mesa(ProductoDeMadera):
    def __init__(self, mueble, tipo, precio,cantLugares):
        ProductoDeMadera.__init__(self,mueble,tipo,precio)
        self.cantLugares = cantLugares

class Banqueta(ProductoDeMadera):
    def __init__(self, mueble, tipo, precio, respaldo):
        ProductoDeMadera.__init__(self,mueble,tipo,precio)
        self.respaldo = respaldo


class Operaciones():
    def __init__(self):
        self.listaSillas = []
        self.listaMesa = []
        self.listaBanquetas = []

        archivo = open("stock_muebles.csv","r")
        info = archivo.readlines()
        archivo.close()
        info.pop(0)

        for x in info:
            a = x.split(",")
            mueble,tipo,precio,peso,cantLugares,respaldo = a
            if x.find("silla") == 0:
                silla = Silla(mueble,tipo,precio,peso)
                self.listaSillas.append(silla)
            elif x.find("mesa") == 0:
                mesa = Mesa( mueble, tipo, precio,cantLugares)
                self.listaMesa.append(mesa)
            elif x.find("banqueta") == 0:
                banqueta = Banqueta( mueble, tipo, precio, respaldo)
                self.listaBanquetas.append(banqueta)
        self.listaTotal = self.listaSillas + self.listaMesa + self.listaBanquetas

    def agregarInfoTexto(self,infoAGuardar):
        archivo = open ("stock_muebles.csv","a")
        archivo.write(infoAGuardar)
        archivo.close


    def agregarMueble(self):
        cond = input("desea agregar mueble (si/no): ")
        while cond == "si":
            mueble = input("que mueble desea agregar (silla/mesa/banqueta): ")
            if mueble == "silla" :
                tipo = input("ingrese el tipo(baja/alta): ")
                precio = input("ingrese el precio: ")
                peso = input("ingrese el peso: ")
                stock = mueble + "," + tipo + "," + precio + "," + peso + ",,\n"
            elif mueble == "mesa" :
                tipo = input("ingrese el tipo(cuadradas/rectangulares): ")
                precio = input("ingrese el precio: ")
                cantLugares = input("ingrese cantidad de lugares: ")
                stock = mueble + "," + tipo + "," + precio + ",," + cantLugares + ",\n"
            elif mueble == "banqueta":
                tipo = input("ingrese el tipo(fija/regulable): ")
                precio = input("ingrese el precio: ")
                respaldo = input("ingrese si tiene respaldo (si/no)")
                stock = mueble + "," + tipo + "," + precio + ",,," + respaldo +"\n"
        
        self.agregarInfoTexto(stock)
    
    def precioMayor(self):
        
        precioBuscado = int(input("ingrese el precio base para buscar: "))
        print("Los muebles con un precio mayor a $",precioBuscado," son:")
        for mueb in self.listaTotal:
            if int(mueb.precio) >= precioBuscado :
                print("Mueble:",mueb.mueble,", Tipo:",mueb.tipo,", Precio: $",mueb.precio)

    def cantMuebleBuscado(self):
        mueb = input("que mueble desea buscar (silla/mesa/banqueta): ")
        if mueb == "silla":
            tip = input("ingrese el tipo(baja/alta): ")
        elif mueb == "mesa":
            tip = input("ingrese el tipo(cuadradas/rectangulares): ")
        elif mueb == "banqueta":
            tip = input("ingrese el tipo(fija/regulable): ")
        stock = 0
        for x in self.listaTotal:
            if x.mueble == mueb:
                if x.tipo == tip:
                    stock += 1
        print("catidad de ",mueb," ",tip)
        print("Mueble: ",mueb," Tipo:",tip," Stock:",stock)

if __name__=="__main__":
    print("Hola")
    op = ""
    while op != 4:
        print("presione el numero de lo operacion a realezar:")
        print("1) Agregar mueble al stock")
        print("2) Consultar los artículos mayores a un precio solicitado")
        print("3) Contar la cantidad de cada mueble discriminado por tipo")
        print("4) Salir")
        op = input("Ingrese opcion deseada: ")
        if op == "1":
            operacion = Operaciones()
            operacion.agregarMueble()
        elif op == "2":
            operacion = Operaciones()
            operacion.precioMayor()
        elif op == "3":
            operacion = Operaciones()
            operacion.cantMuebleBuscado()
        elif op == "4":
            print("Chau")
        else:
            print("la opcion es incorrecta")
