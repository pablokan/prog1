def sumaOresta(n1, n2, op):
    r=0
    if op == '+':
        r = n1 + n2
    else:
        r = n1 - n2
    return r

print(sumaOresta(1, 2, '+'))
print(sumaOresta(1, 2, '-'))

def suma(n1, n2):
    return n1 + n2

def raya(caracter, cantidad):
    for x in range(cantidad):
        print(caracter, end='')
    print()

raya('*', 10)
raya('+', 20)

print('hola', end='*') 
print('chau')
