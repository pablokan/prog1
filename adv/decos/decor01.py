def raya(f):
    def r(*args):
        f(*args)
        cant = 5 + len(args[0])
        for x in range(cant):
            print('+', end='')
        print()
    return r


@raya
def hola(nombre):
    print(f"Hola {nombre}")

hola('Juan')
hola('Rigoberto Esmeralda')