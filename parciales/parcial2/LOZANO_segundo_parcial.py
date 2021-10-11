class Mueble():
    def nombreMueble(self):
        print('------ AGREGAR MUEBLE ------')
        self.mueble = input('Que mueble quiere agregar: (MESA/BANQUETA/SILLA) ')
        self.mueble = self.mueble.lower()
        
    def precioPedido(self):
        print('------ ARTICULOS MAYORES A UN PRECIO ------')
        self.prec = int(input('Que precio desea consultar: '))
   
    
    def agregarMueble(self,agregar):
        self.agregar = agregar
        self.tipo = input('Ingrese el tipo: ').lower()
        self.precio = int(input('Ingrese el valor: '))
        self.string = self.mueble + ',' + self.tipo + ',' + str(self.precio) + ',,,\n'
        self.agregar.append(self.string)


    def precioMayor(self,datos,mayores):
        self.datos = datos
        self.mayores = mayores
        for x in self.datos:
            self.coma = x.find(',')
            self.segundaComa = x.find(',',self.coma+1)
            self.tercerComa = x.find(',',self.segundaComa+1)
            self.mue = x[:self.coma]
            self.tipo = x[self.coma+1:self.segundaComa]
            self.pre = x[self.segundaComa+1:self.tercerComa]
            if int(self.pre) > int(self.prec):
                self.agregarStr = 'Mueble:' + self.mue + ', Tipo:' + self.tipo + ', Precio: $' + str(self.pre)
                self.mayores.append(self.agregarStr)
        for t in mayores:
            print(t)
    
    def cantMuebles(self,cantidad,datos):
        print('----- CANTIDAD STOCK -----')
        self.cant = cantidad
        self.datos = datos
        for e in self.datos:
            coma = e.find(',')
            segundaComa = e.find(',',coma+1)
            tercerComa = e.find(',',segundaComa+1)
            mue = e[:coma]
            tipo = e[coma+1:segundaComa]
            pre = int(e[segundaComa+1:tercerComa])
            if tipo == 'cuadrada':
                self.cant['mesa']['cuadrada'] += 1
            if tipo == 'rectangular':
                self.cant['mesa']['rectangular'] += 1
            if tipo == 'alta':
                self.cant['silla']['alta'] += 1
            if tipo == 'baja':
                self.cant['silla']['baja'] += 1
            if tipo == 'fija':
                self.cant['banqueta']['fija'] += 1
            if tipo == 'regulable':
                self.cant['banqueta']['regulable'] += 1

    def mostrarMuebles(self):
        for x, y in self.cant.items():
            print('Muble:',x, ' Tipos:' , y)





if __name__ == '__main__':
    mayores = []
    cant = {'mesa': {'cuadrada':0,'rectangular':0},'silla': {'alta':0,'baja':0}, 'banqueta': {'fija':0 , 'regulable':0}}
    m = open('stock_muebles.csv','a')
    c = open('stock_muebles.csv','r')
    c = c.readlines()
    c.pop(0)
    m1 = Mueble()
    m1.nombreMueble()
    m1.agregarMueble(c)
    m1.precioPedido()
    m1.precioMayor(c,mayores)
    m1.cantMuebles(cant,c)
    m1.mostrarMuebles()
