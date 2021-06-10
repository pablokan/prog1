# funciones ya conocidas 
# (todas las funciones en Python son first-class)
# print, input, int

a = [int, print, list.append]
print(a[0]('12')*2)
a[1]('chau')
l = []
a[2]('dsds')
print(l)




def f1():
    print('++++++++++++++++')
f1()
print('Hola')
f1()

def f2():
    return '===================='
print(f2())

def f3(n):
    return n * 2
print(f3(2))
print(f3('hola'))

def f4(nombre, edad):
    print('Hola', nombre, 'tenés', edad, 'años')
f4('Juan', 31)

def f5(nombre, edad=1000):
    print(nombre, edad)
f5('Juan', 31)
f5('Pablo')






