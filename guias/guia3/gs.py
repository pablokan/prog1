listaNumero = []
contador= 0
for x in range(10):
     numeroIngresado = int(input('Ingrese un numero:'))
     if numeroIngresado > 23:
         contador = contador + 1
         listaNumero.append(numeroIngresado)

print ('la cantidad de mayores de 23 es: ',contador) 
print(listaNumero)       


