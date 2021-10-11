from repertorio_de_funciones import inputNumber

class Mueble():
    def __init__(self,nombre,valor,tipo):
        self.valor = valor
        self.tipo = tipo
        self.nombre = nombre

    def getValor(self):
        return self.valor
    
    def getTipo(self):
        return self.tipo
    
    def getName(self):
        return self.nombre

class Silla(Mueble):
    def __init__(self,valor,tipo,nombre):
        super().__init__(valor,tipo,nombre)

class Banqueta(Mueble):
    def __init__(self,valor,tipo,nombre):
        super().__init__(valor,tipo,nombre)

class Mesa(Mueble):
    def __init__(self,valor,tipo,nombre):
        super().__init__(valor,tipo,nombre)

class FabricaMuebles():
    mueblesStock=[]
    muebles=[]
    with open("stock_muebles.csv") as file:
        line=file.readline()
        while line:
            line=file.readline()
            for x in (line[:-1].split(",")[:3]):
                if x=="mesa":
                    muebles.append(Mesa("mesa",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))
                    mueblesStock.append(Mesa("mesa",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))
                elif x=="banqueta":
                    muebles.append(Banqueta("banqueta",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))
                    mueblesStock.append(Banqueta("banqueta",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))
                elif x=="silla":
                    muebles.append(Silla("silla",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))
                    mueblesStock.append(Banqueta("banqueta",line[:-1].split(",")[:3][2],line[:-1].split(",")[:3][1]))

    def menuMuebles(self):
        eleccion=0
        while eleccion!=5:
            eleccion=inputNumber("\n1-Ver stock.\n2-Agregar stock.\n3-Consultar articulos mayor a un precio solicitado.\n4-Cantidad de muebles por tipo.\n5-Salir.\nSeleccione opcion 1-5: ","entero",min=1,max=5)
            if eleccion==1:
                self.getMueblesStock()
            elif eleccion==2:
                self.getMuebles()
                self.agregarMuebles()
            elif eleccion==3:
                self.mayorPrecio()
            elif eleccion==4:
                self.cantMueblesTipo()
                
    def getMuebles(self):
        num=1
        for x in self.muebles:
            print(f"{num}-Nombre:{x.getName()}. Precio: {x.getValor()}. Tipo: {x.getTipo()}.")
            num+=1
    
    def getMueblesStock(self):
            num=1
            for x in self.mueblesStock:
                print(f"{num}-Nombre: {num}-{x.getName()}. Precio: {x.getValor()}. Tipo: {x.getTipo()}.")
                num+=1
    
    def agregarMuebles(self):
        opcion=inputNumber("11-Salir.\nSeleccione mueble para agregar al stock[1-11]: ","entero",1,11)
        if opcion!=11: self.mueblesStock.append(self.muebles[opcion-1])
                
    def mayorPrecio(self):
        precio=inputNumber("Ingrese precio base: ","entero",0,99999990)
        for x in self.mueblesStock:
            if int(x.getValor())>precio: print(f"-Nombre:{x.getName()}. Precio: {x.getValor()}. Tipo: {x.getTipo()}.")
    
    def cantMueblesTipo(self):
        cant=0
        tipoMueble=input("Ingrese tipo de mueble[cuadrada-rectangular-fija]: ")
        for x in self.mueblesStock:
            if x.getTipo()==tipoMueble:cant+=1
        print(f"Cantidad de muebles tipo {tipoMueble}: {cant}.")


if __name__ == '__main__':
    mueblesEze=FabricaMuebles()
    mueblesEze.menuMuebles()