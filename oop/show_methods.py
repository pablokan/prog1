cadena = "Hola"

def ownMethods(o):
    print('\n', o, 'own methods:')
    for m in dir(o):
        if not m.startswith("__") and m != None:
            print(m, end=' ')

print(ownMethods(cadena))
