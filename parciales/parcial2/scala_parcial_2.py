class Muebles():
    def __init__(self, listaMuebles):
        self.listaMuebles = listaMuebles

    def agMueble(self, tipo, caracteristica, precio):
        listaMuebles = []
        articulo = []
        self.tipo = tipo
        self.caracteristica = caracteristica
        self.precio = precio
        articulo.append(self.tipo)
        articulo.append(self.caracteristica)
        articulo.append(self.precio)
        listaMuebles.append(articulo)

    def conPrecio(self, precioConsulta):
        self.precioConsulta = precioConsulta
        for mueble in self.listaMuebles:
                if int(mueble[2]) >= self.precioConsulta:
                    print('Mueble:', mueble[0], 'Tipo:', mueble[1], 'Precio: $', mueble[2])
                

    def conStock(self, tipo, caracteristica):
        self.tipo = tipo
        self.caracteristica = caracteristica
        cantidad = 0 
        for mueble in self.listaMuebles:
                if mueble[0] == self.tipo and mueble[1] == self.caracteristica:
                    cantidad = cantidad + 1 
        print('Mueble:', self.tipo, 'Tipo:', self.caracteristica, 'Cantidad:', cantidad)


if __name__ == "__main__":
    lista1 = []
    archivo = open('stock_muebles.csv', 'r')
    listaMuebles = archivo.readlines()
    for x in listaMuebles:
        pos = x.find('mueble')
        if pos != 0:
            mueble = x.split(',')
            m = []
            m.append(mueble[0])
            m.append(mueble[1])
            m.append(mueble[2])
            lista1.append(m)
    
    print(lista1)
    a = Muebles(lista1)
    a.agMueble('silla', 'baja', '12001')
    print('Resultado de la consulta:')
    a.conPrecio(12000)
    print('Consultando stock:')
    a.conStock('banqueta', 'fija')