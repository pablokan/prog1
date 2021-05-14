preg1 = input('¿Desea ingresar una letra? ')

c = 0
letras = []

while preg1 == 'si':
    l = input('Ingrese una letra: ')
    letras.append(l)
    preg1 = input('¿Desea ingresar otra letra? ')

for x in letras:
    if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
        c = c + 1 
    

fin = print('La cantidad de vocales ingresadas es: ',c)