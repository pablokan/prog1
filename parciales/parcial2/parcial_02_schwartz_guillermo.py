import csv
archivo= open('stock_muebles.csv','r',encoding='utf-8')
stockFinal=[]
for lineal in archivo:
    stockFinal.append(lineal.strip().split(","))

class Muebles():
    def __init__(self,nombre,tipo,precio):
        self.nombre=nombre
        self.tipo=tipo
        self.precio=precio
    def getNombre(self):
        return self.nombre
    def getTipo(self):
        return self.tipo
    def getPrecio(self):
        return self.precio

class Banquetas(Muebles):
    def __init__(self,nombre,tipo,precio): 
        super().__init__(nombre,tipo,precio)
        
class Mesas(Muebles):
    def __init__(self,nombre,tipo,precio):
        super().__init__(nombre,tipo,precio)

class Sillas(Muebles):
    def __init__(self,nombre,tipo,precio):
        super().__init__(nombre,tipo,precio)

class NuevoStock():
    def __init__(self,stocksillas=[]):
        self.stocksillas = stocksillas
        self.stockFinalSillas = [] + self.stocksillas 
        self.stockmesas= []
        self.stockbanquetas= []
        self.muebles = [] + self.stocksillas 
        stockInicio=stockFinal[1:]

        for stock in stockInicio:
            nombre,tipo,precio=stock[0:3]  
            mueble=Muebles(nombre,tipo,precio)
            self.muebles.append(mueble)
            if nombre=="silla":
                nuevo=Sillas(nombre,tipo,precio)
                self.stockFinalSillas.append(nuevo)
            elif nombre=="mesa":
                nuevo=Mesas(nombre,tipo,precio)
                self.stockmesas.append(nuevo)
            elif nombre=="banqueta":
                nuevo=Banquetas(nombre,tipo,precio)
                self.stockbanquetas.append(nuevo)  
 
    def muestroSillas(self): 
        for silla in self.stockFinalSillas:
            print(f"Tipo:",silla.getTipo(),"Precio:",silla.getPrecio())

    def muestroMesas(self):
        for mesa in self.stockmesas:
            print(f"Tipo:",mesa.getTipo(),"Precio:",mesa.getPrecio())

    def muestroBanquetas(self):
        for banqueta in self.stockbanquetas:
            print(f"Tipo:",banqueta.getTipo(),"Precio:",banqueta.getPrecio())

    def muestroPrecio(self):
        for xi in self.muebles:
            if int(xi.getPrecio())>int(12000):
                print(f"Mueble:",xi.getNombre(),"Tipoes:",xi.getTipo(),"Precio:",xi.getPrecio())

    def muestroBanquetaPedido(self):
        banquetasFijas=[x for x in self.stockbanquetas if x.getTipo()=="fija"] 
        for fija in banquetasFijas:
            return print(f"Mueble:",fija.getNombre(),end=" "),print("Tipoes:",fija.getTipo(),end=" "),print("Stock:",len(banquetasFijas))

silla=Sillas("silla","baja",12001)
muestreo=NuevoStock([silla])
muestreo.muestroBanquetas()
muestreo.muestroMesas()
muestreo.muestroPrecio()
muestreo.muestroBanquetaPedido()
muestreo.muestroSillas()