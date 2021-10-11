# programadores pumas 

archivo = open("stock_muebles.csv", "r")

lineas = archivo.readlines()
lineas.pop(0)


class Muebles():

    def __init__(self,mueble, tipo, precio):
        self.__mueble = mueble
        self.__tipo = tipo
        self.__precio = precio

    @property   # esto hace que sea un get  
    def mueble(self):
        return self.__mueble
    
    @mueble.setter  # esto hace que sea un set
    def mueble(self, valor):
        self.__mueble = valor 
        
    @property    
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor 
        
    @property    
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor 
    

    def __str__(self):
        return "mueble " + str(self.__mueble) + " tipo " + str(self.__tipo) + " precio " + str(self.__precio)

class Agregar_muebles():
    def __init__(self):
        self.mueble = []
        self.tipo = []
        self.precio = [] 
            
    def añadir_productos(self, mueble, tipo, precio):
        self.mueble.append(mueble)
        self.tipo.append(tipo)
        self.precio.append(precio)

        for (m,t,p) in zip(self.mueble, self.tipo, self.precio):
            archivo = open('stock_muebles.csv','a') 
            archivo.writelines(m,t,p)
    

class Consultar_precio():
    pass
