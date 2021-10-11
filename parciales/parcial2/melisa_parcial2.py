class Valor():
    def __init__(self, precio):
        self.precio = precio

class Mesa(Valor):
    def __init__(self, mueble, tipo, precio):
        Valor.__init__(self, precio)
        self.mueble = mueble
        self.tipo = tipo

class Silla(Valor):
    def __init__(self, mueble, tipo, precio):
        Valor.__init__(self, precio)
        self.mueble = mueble
        self.tipo = tipo

class Banqueta(Valor):
    def __init__(self, mueble, tipo, precio):
        Valor.__init__(self, precio)
        self.mueble = mueble
        self.tipo = tipo

class Fabrica():
    def __init__(self):
        self.listaObjetosMuebles = []
        self.precioMuebles = []

        f = open("stock_muebles.csv", 'r', encoding="utf-8")
        lineas = f.readlines()
        lineas.pop(0)
        for li in lineas:
            li = li[:-1].split(',') # le saco el último caracter (salto de línea)       
            if li[0] >= "mesa":
                mueble = li[0]
                tipo = li[1]
                precio = li[2]
                self.precioMuebles.append(precio)
                agrega = Mesa(mueble,tipo,precio)
                self.listaObjetosMuebles.append(agrega)
            elif li[0] >= "silla":
                mueble = li[0]
                tipo = li[1]
                precio = li[2]
                self.precioMuebles.append(precio)
                agrega2 = Silla(mueble, tipo, precio)
                self.listaObjetosMuebles.append(agrega2)
            elif li[0] >= "banqueta":
                mueble = li[0]
                tipo = li[1]
                precio = li[2]
                self.precioMuebles.append(precio)
                agrega3 =  Banqueta(mueble, tipo, precio)
                self.listaObjetosMuebles.append(agrega3)
        f.close()
    
        new_list = []
        self.precioMuebles.pop(0)
        for i in self.precioMuebles:
            new_list.append(int(i))

        self.precioMuebles = new_list

    def consultaPorRangoDeUnPrecioIndicado(self):
        precioMasBajo = min([precio for precio in self.precioMuebles])
        precioMasAlto = max([precio for precio in self.precioMuebles])
        print(f"\nLos precios rondan desde ${precioMasBajo} hasta ${precioMasAlto}")
        valorAconsultar = int(input("Indique un precio para consultar disponibles: "))
        for objeto in self.listaObjetosMuebles:
            for precio in self.precioMuebles:
                if precio <= valorAconsultar and str(precio) == objeto.precio:
                    print("Mueble: ", objeto.mueble, ", Tipo: ", objeto.tipo, ", Precio: $", objeto.precio)
        print()
        
    def agregarMueble(self):
        file = open("stock_muebles.csv","a", encoding="utf-8")
        mueble = input("Ingrese mueble a cargar: ")
        tipo = input("Indique tipo del mueble ingresado: ")
        precio = input("Indique precio del mueble: ")
        file.write("\n" + mueble + "," + tipo + "," + precio)
        file.close()
            

    def contarCantidadMueblesPorTipo(self):
        print("\nVenta de muebles: \nMesa: cuadrada - rectangular - redonda\nSilla: baja - alta\nBanqueta: fija - regulable")
        muebleConsulta = input("\nIndique mueble a consultar: ")
        tipoConsulta = input("Indique tipo del mueble consultado: ")
        contador = 0
    
        for objeto in self.listaObjetosMuebles:
            if objeto.tipo == tipoConsulta:
                contador = contador + 1      

        print(f"Mueble: {muebleConsulta} Tipo: {tipoConsulta} Stock: {contador}")  

if __name__ == '__main__':
    f = Fabrica()
    f.consultaPorRangoDeUnPrecioIndicado()
    f.agregarMueble()
    f.contarCantidadMueblesPorTipo()