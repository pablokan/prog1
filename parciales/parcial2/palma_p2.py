abrir=open("stock_muebles.csv","r",encoding="utf-8")
stocktotal=[]
for line in abrir:
    stocktotal.append(line.strip().split(","))
# ------------------------------------------------------------------------------------------
class Muebles():
    def __init__(self,nombre,formato,precio):
        self.nombre=nombre
        self.formato=formato
        self.precio=precio
    def getNombre(self):
        return self.nombre
    def getFormato(self):
        return self.formato
    def getPrecio(self):
        return self.precio
# ------------------------------------------------------------------------------------------
class Sillas(Muebles):
    def __init__(self,nombre,formato,precio): 
        super().__init__(nombre,formato,precio)
class Mesas(Muebles):
    def __init__(self,nombre,formato,precio):
        super().__init__(nombre,formato,precio)
class Banquetas(Muebles):
    def __init__(self,nombre,formato,precio):
        super().__init__(nombre,formato,precio)
# ------------------------------------------------------------------------------------------
class Agregarstock():
    def __init__(self,stocksillas=[]):
        self.stocksillas = stocksillas
        stockinicial=stocktotal[1:] #ELIMINO EL PRIMER RENGLON DE LA LISTA STOCKTOTAL
        self.muebles = [] + self.stocksillas #lista de objetos muebles
# ------------------------------------------------------------------------------------------ 
        for s in stockinicial:
            nombre,formato,precio=s[0:3] #Tomo los datos relevantes para el enunciado. 
            mueble=Muebles(nombre,formato,precio)#Instancio Muebles
            self.muebles.append(mueble)
# ------------------------------------------------------------------------------------------
    def mostrarTodoSegunPrecio(self):#Metodo para ver los muebles en stock segun un precio tope
        for x in self.muebles:
            if int(x.getPrecio())>int(12000):
                print(f"Mueble:",x.getNombre(),"Tipo:",x.getFormato(),"Precio:",x.getPrecio())
# ------------------------------------------------------------------------------------------
    def mostrarBanquetaSegunLoPedido(self):#Metodo para ver las banquetas que cumplan cierto criterio. 
        banquetasfijas=[x for x in self.muebles if x.getFormato()=="fija"] 
        for z in banquetasfijas:
            return print(f"Mueble:",z.getNombre(),end=" "),print("Tipo:",z.getFormato(),end=" "),print("Stock:",len(banquetasfijas))
# ------------------------------------------------------------------------------------------
    def mostrarMueble(self,mueble=""): 
        for x in self.muebles:
            if mueble=="":
                print(f"Mueble:",x.getNombre(),"Tipo:",x.getFormato(),"Precio:",x.getPrecio())
            elif  x.getNombre()==f"{mueble}":
                print(f"Tipo:",x.getFormato(),"Precio:",x.getPrecio())

silla=Sillas("silla","baja",12001)
nuevo=Agregarstock([silla])
nuevo.mostrarTodoSegunPrecio()
nuevo.mostrarBanquetaSegunLoPedido()
nuevo.mostrarMueble("silla")
