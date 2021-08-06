from input_int import inputInt

def opc1():
    print('opción 1')

def opc2():
    print('opción 2')

def menu():
    op = 0
    while op != 3:
        print('1. Primera')
        print('2. Segunda')
        print('0. Salir')
        op = inputInt('Opción: ', min=1, max=3)
        if op == 1:
            opc1()
        elif op == 2:
            opc2()

menu()
