numero1 = int(input('Ingrese el primero numero por favor: '))
numero2 = int(input('Ingrese el segundo numero por favor: '))
operacion = input('Ingrese la operacion que quiere realizar, "+" o "-":')

if operacion == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operacion == '-':
    resultado = numero1 - numero2
    print(resultado)
else:
    print('Error')
    