import sys

def inputInt(mensaje, min=-sys.maxsize, max=sys.maxsize):
    numero = 0
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
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
    n = inputInt('Ingrese un entero entre 3 y 7: ', 3, 7)
    m = inputInt('Cualquier entero: ')
    maxito = inputInt('ingrese un entero menor a 1000: ', max=999)
    minito = inputInt('ingrese un entero mayor a 1000: ', min=1001)
