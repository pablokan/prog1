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

def inputFloat(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = float(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número real")
    return numero

if __name__ == "__main__":
    a = inputInt('Ingrese un entero: ')
    print('El número entero ingresado es', a)
    b = inputFloat('Ingrese un real: ')
    print('El número real ingresado es', b)

