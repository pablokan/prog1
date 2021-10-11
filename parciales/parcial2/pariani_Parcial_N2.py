from dataclasses import dataclass

csv = open("stock_muebles.csv", "r")
texto = csv.readlines()
# falta utilizar el stock del .csv


@dataclass
class muebles:
    Mueble: str
    formato: str
    precio: int

    def getMFP(self):
        return f"\n{self.Mueble}      {self.formato}        {self.precio}"


@dataclass
class silla(muebles):
    pesoLim: int

    def getPesoLim(self):
        return f"    {self.pesoLim} (kg)   "


@dataclass
class mesas(muebles):
    Lugares: int

    def getLugares(self):
        return f"      {self.Lugares}     "


@dataclass
class banquetas(muebles):
    respaldo: str

    def getrespaldo(self):
        return f"   {self.respaldo}   "


@dataclass
class main:

    listaDeMuebles = []

    mueble = input("Que tipo de mueble es: ")
    formato = input("Que formato: ")
    precio = int(input("Precio: "))

    if mueble == "mesa":
        personas = int(input("Cantidad de Personas: "))
        Mu1 = mesas(mueble, formato, precio, personas)
        MFP = Mu1.getMFP()
        lugares = Mu1.getLugares()

        final = MFP + lugares

    elif mueble == "silla":
        pesoLim = int(input("peso limite: "))
        Mu1 = silla(mueble, formato, precio, pesoLim)
        MFP = Mu1.getMFP()
        peso = Mu1.getPesoLim()

        final = MFP + peso

    elif mueble == "banqueta":
        resp = input("tiene respaldo: (si) (no)")
        Mu1 = banquetas(mueble, formato, precio, resp)
        MFP = Mu1.getMFP()
        respaldo = Mu1.getrespaldo()

        final = MFP + respaldo

    txt = open("muebles.csv", "a")
    txt.write(final)
    txt.close()

    listaDeMuebles.append(Mu1)

    MuebleElejido = input("Que mueble quiere buscar: ")

    if MuebleElejido == "mesa":
        filtro = input("Que formato quiere buscar: ")
        precio = int(input("A partir de que precio: "))

    elif MuebleElejido == "silla":
        filtro = input("Que formato quiere buscar: ")
        precio = int(input("A partir de que precio: "))

    elif MuebleElejido == "banqueta":
        filtro = input("Que formato quiere buscar: ")
        precio = int(input("A partir de que precio: "))

    for x in listaDeMuebles:

        if x.formato == filtro and x.precio >= precio:
            print(x.Mueble, x.formato, x.precio)


if __name__ == "__main__":
    main()
