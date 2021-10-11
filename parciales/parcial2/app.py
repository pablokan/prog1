class Mueble:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio


class Mesa(Mueble):
    def __init__(self, nombre, tipo, precio, personas):
        super().__init__(nombre, tipo, precio)
        self.personas = personas


class Silla(Mueble):
    def __init__(self, nombre, tipo, precio, peso):
        super().__init__(nombre, tipo, precio)
        self.peso = peso


class Banqueta(Mueble):
    def __init__(self, nombre, tipo, precio, respaldo):
        super().__init__(nombre, tipo, precio)
        self.respaldo = respaldo


class Muebleria:
    def __init__(self):
        stock = open("stock_muebles.csv", "r")
        self.muebles = []
        stock.readline()
        for line in stock:
            datos = line[:-1].split(",")
            if datos[0] == "mesa":
                mueble = Mesa("mesa", datos[1], datos[2], datos[4])
            elif datos[0] == "silla":
                mueble = Silla("silla", datos[1], datos[2], datos[3])
            elif datos[0] == "banqueta":
                mueble = Banqueta("banqueta", datos[1], datos[2], datos[5])
            self.muebles.append(mueble)

    def agregarMueble(self, nombre, tipo, precio):
        self.muebles.append(Mueble(nombre, tipo, precio))

    def masCaros(self, precio):
        for mueble in self.muebles:
            if int(mueble.precio) > precio:
                print(
                    f"Mueble: {mueble.nombre}, Tipo: {mueble.tipo}, Precio: ${mueble.precio}"
                )

    def verStock(self, nombre, tipo):
        print("\nCantidad en existencia")
        c = 0
        for mueble in self.muebles:
            if mueble.nombre == nombre and mueble.tipo == tipo:
                c += 1
        print(f"Mueble: {nombre} Tipo: {tipo} Stock: {c}")


muebleria = Muebleria()
muebleria.agregarMueble("silla", "baja", 12001)
muebleria.masCaros(12000)
muebleria.verStock("banqueta", "fija")
