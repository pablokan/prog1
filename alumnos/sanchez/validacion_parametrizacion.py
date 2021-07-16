from validador import inputNumber, inputMail, concatenacion, inputOp, creaMenu, selecta, inputDate, inputLstring
menuopcional=False

while not menuopcional:
      
    import os
    os.system('cls')

    print(' * * * SELECCIONE UNA  OPCIÓN A VALIDAR * * *')
    creaMenu(A=" 1 - Concatenar un número indeterminado de strings con un caracter determinado (por defecto un espacio)", B=" 2 - Validar una dirección de correo electrónico", C=" 3 - Input de fechas (validar formato y devolver año, mes y día como enteros), debe forzar un formato estricto, por ejemplo dd/mm/aaaa", D=" 4 - Input de strings (validar largo por al menos 8 caracteres, y no mas de 14): ", F=" 5 - Final")

    number=inputNumber('Seleccione una opción del 1 al 6 : ')  # 2) Validar un entero (reutilizar inputInt) con rango opcional.

    numero=selecta(number)

    if numero == 1:
        print(concatenacion('hola', 'libreria', 'formatos', 'etcetera', sep=' '))
        menuopcional=inputOp('Continúa (s/n): ')
    elif numero == 2:
        email=inputMail('Ingrese su correo electrónico: ') # 3) Validar una dirección de correo electrónico
        print('La casilla ', email, ' es válida')
        menuopcional=inputOp('Continúa (s/n): ')
    elif numero == 3:
        fecha=inputDate('Ingrese una fecha: (dd/mm/aaaa) ')
        menuopcional=inputOp('Continúa (s/n): ')
    elif numero == 4:
        longString=inputLstring('Ingrese una cadena de al menos 3 caracteres, y no mas de 6: ')
        print('La cadena ', longString, 'está validada.')
        menuopcional=inputOp('Continúa (s/n): ')
    elif numero == 5:
        menuopcional= True

print('Listo')        


