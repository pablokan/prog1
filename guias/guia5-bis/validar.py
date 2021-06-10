# Ejemplo de carga con edad (entero) y altura (real)
# Validar (código repetido)

validado = False
while not validado:
    n = input('Número 1: ')
    try:
        n = int(n)
        validado = True
    except:
        print('Incorrecto. Ingrese un entero')

validado = False
while not validado:
    m = input('Número 2: ')
    if m.isdigit():
        validado = True
    else:
        print('Incorrecto. Ingrese un entero')







