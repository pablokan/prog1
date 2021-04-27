#Pedir nombres y sexo de personas y 
# mostrar el total de mujeres 
# y el nombre de cada una.

c = 0
for x in range(3):
    nombre = input('Nombre: ')
    sexo = input('Sexo: ')
    if sexo == 'f':
        print(nombre)
        c = c + 1
print('Hay', c, 'mujeres')

