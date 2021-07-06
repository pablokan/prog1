from valids import iI

def menu(**ops):
    print('\n----------------------')
    print('Menú', end='\n\n')
    d = {}
    cantItems = len(ops) + 1
    op = 0
    while op != cantItems:
        for i,v in enumerate(ops.items(), start=1):
            print(i, ')', v[1])
            d[i] = v[0]
        print(cantItems, ') Salir del Programa')
        op = iI('Opción: ', min=1, max=cantItems)
        if op != cantItems:
            eval(d[op]+'()')

def stop():
    input('Enter para volver al menú')

def createUser():
    print('función createUser')
    stop()

def delUser():
    print('función delUser')
    stop()

def listUsers():
    print('función listUsers')
    stop()

menu(createUser='Crear usuario!', delUser='Borrar usuario', listUsers='Listar usuarios')

