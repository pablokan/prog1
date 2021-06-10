import os
os.system('cls')
Numero = int(input('Ingrese un número de cualquier extensión: '))
if Numero>0:
    contador = len(str(Numero))
    print('El número ingresado tiene %s dígitos' % (contador))
else:
    print('El número es negativo')
