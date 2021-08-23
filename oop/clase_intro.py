class Operacion:
    def tomar(self):
        self.n1 = input("Ingrese un numero: ")
        self.n2 = input("Ingrese otro numero: ")

    def operar(self):
        self.resultado = None

    def mostrar(self):
        return self.resultado


class Suma(Operacion):
    def operar(self):
        self.resultado = int(self.n1) + int(self.n2)

""" 
s = Suma()
s.tomar()
s.operar()
print(s.mostrar())

"""
cadena = "Hola"
suma = Suma()

def ownMethods(o):
    print('\n', o, 'own methods:')
    for m in dir(o):
        if not m.startswith("__") and m != None:
            print(m, end=' ')

print(ownMethods(cadena), ownMethods(suma))