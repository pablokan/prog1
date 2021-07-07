def inputInt2(mensaje, min=None, max=None):
    numero = 0
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if min == max == None:
                validado = True
            else:
                if (min != None and max != None):
                    validado = True if (min <= numero <= max) else print('El rango de valores es entre', min, 'y', max)
                elif min != None:
                    validado = True if (min <= numero) else print('Debe ser mayor que', min-1)
                elif max != None:
                    validado = True if (numero <= max) else print('Debe ser menor que', max+1)
                
        except:
            print("Error. Debe ingresar un número entero")
    return numero


if __name__ == '__main__':
    n = inputInt2('Ingrese un entero entre 3 y 7: ', 3, 7)
    m = inputInt2('Cualquier entero: ')
    maxito = inputInt2('ingrese un entero menor a 1000: ', max=999)
    minito = inputInt2('ingrese un entero mayor a 1000: ', min=1001)
