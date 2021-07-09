def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero



def validacion_entero(message='Imgrese un numero entre 0 y 99999: ', min=0,max=99999):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    try:  
        numero = inputNumber('entero',message)
        while numero < min or numero > max:
            numero = inputNumber('entero', message)
        return numero
    except:
        return 'Error, argumento invalido'


print(validacion_entero('ingrese un entero mayor a 1000: ',min=1001))

    
        
    