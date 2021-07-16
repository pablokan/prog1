infinite = 1e309  # actual python infinite
def inputNumber(dataType, mensaje, min=-infinite, max=infinite):
    sufijoMensaje = ''
    tipoNum = {int: 'entero', float: 'real'}
    if min != -infinite and max != infinite:
        sufijoMensaje = f'(entre {min} y {max})'
    elif min != -infinite:
        sufijoMensaje = f'(mayor a {min-1})'
    elif max != infinite:
        sufijoMensaje = f'(menor a {max+1})'
    mensaje = f'{mensaje} {sufijoMensaje}: '
    numero = ''
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = dataType(numero)
            if min <= numero <= max:
                validado = True
            else:
                print('valor fuera de rango')
                
        except:
            print(f"Error. Debe ingresar un número {tipoNum[dataType]}")
    return numero


if __name__ == '__main__':
    i = inputNumber(int, 'Ingrese una edad', 13, 17)
    print(type(i))
    r = inputNumber(float, 'Ingrese una altura', 1.55, 1.75)
    print(r, type(r))
    m = inputNumber(int, 'Cualquier entero')
    maxito = inputNumber(int, 'ingrese un entero bajo', max=999)
    minito = inputNumber(float, 'ingrese un real alto', min=1001)

