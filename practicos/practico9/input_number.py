import sys

def inputNumber(dataType, mensaje, min=-sys.maxsize, max=sys.maxsize):
    numero = 0
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = dataType(numero)
            if min <= numero <= max:
                validado = True
            else:
                if min != -sys.maxsize and max != sys.maxsize:
                    print('El rango de valores es entre', min, 'y', max)
                elif min != -sys.maxsize:
                    print('Debe ser mayor que', min-1)
                elif max != sys.maxsize:
                    print('Debe ser menor que', max+1)
                
        except:
            print("Error. Debe ingresar un número entero")
    return numero


if __name__ == '__main__':
    i = inputNumber(int, 'Ingrese un entero entre 3 y 7: ', 3, 7)
    print(type(i))
    r = inputNumber(float, 'Ingrese un real entre 3 y 7: ', 3, 7)
    print(r, type(r))
    # m = inputNumber('Cualquier entero: ')
    # maxito = inputNumber('ingrese un entero menor a 1000: ', max=999)
    # minito = inputNumber('ingrese un entero mayor a 1000: ', min=1001)
    minito = inputNumber(float, 'ingrese un real mayor a 1000: ', min=1001)