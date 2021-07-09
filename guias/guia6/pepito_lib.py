def inputInt(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número entero")
    return numero

def inputStr(mensaje):
    s = input(mensaje)
    return s

if __name__ == '__main__':
    a = inputInt('pruebaaaaaaa: ')
    print(a)


