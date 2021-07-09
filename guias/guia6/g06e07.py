import sys
def inputStr(mensaje='Ingrese una cadena', min=0, max=sys.maxsize):
    s = ''
    mensaje += ": "
    valido = False
    while not valido:
        s = input(mensaje)
        if min <= len(s) <= max:
            print(min, len(mensaje), max)
            valido = True
        else:
            print('Cadena de tamaño fuera de rango')
    return s

if __name__ == '__main__':
    a = inputStr()
    print(a)
    nombre = inputStr('Ingrese su nombre')
    print('Hola', nombre)
    b = inputStr('Ingrese una frase', 10, 20)