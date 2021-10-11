file = open ('stock_muebles.csv', 'r')
read = file.readlines()
read.pop(0)
muebles= []
tipos = []
precios = []
file.close()
for e in read:
    salto = e.split('\n')  
    salto.pop(1)
    for e in salto:
        separar = e.split(',')
        muebles.append(separar[0])           
        tipos.append(separar[1])
        precios.append(int(separar[2]))
      

from zumbi import *
class Muebles():
    def __init__(self,muebles,tipos,precios):
       self.muebles = muebles
       self.tipos = tipos
       self.precios = precios 

class Gestion(Muebles):
    
    def AggMuebles(self):
        
      
        self.mueble_M = input("ingrese el mueble a añadir :")
        self.muebles.append(self.mueble_M)
        self.formato_M = input("ingrese el tipo de mueble : ")
        self.tipos.append(self.formato_M)
        self.precio_M = inputInt("ingrese el precio: ")
        self.precios.append(self.precio_M)
        

    def PrecioArt(self):
        nuevoprecio = inputInt("consultar precio:")
        for x in range(len(self.precios)):
            if nuevoprecio < self.precios[x]:
                print(self.muebles[x],self.tipos[x],self.precios[x])
                

    def CantMueblesxTipo(self):
        self.cuentaRepetidos = {}
        for  numero in self.tipos:
    
            if numero not in self.cuentaRepetidos:
                self.cuentaRepetidos[numero] = 1
                continue

            if self.cuentaRepetidos[numero] == 1:
               self.cuentaRepetidos[numero] += 1

        for x,y in zip(self.muebles,self.cuentaRepetidos.items()):
            tip = y[0]
            cant = y[1]
            print("mueble: ",x,"tipo: ",tip,"cantidad: ",cant)
        

class Op():
 
    compo = Gestion(muebles,tipos,precios)
    compo.AggMuebles()
    compo.PrecioArt()
    compo.CantMueblesxTipo()
    
    
prueba = Op()









