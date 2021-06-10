# 9. Dada una lista cargada con 7 números enteros, 
# obtener el promedio de ellos. 
# Mostrar por pantalla dicho promedio y 
# los números ingresados que sean mayores que él. 
# Dos funciones: promedio y mayorQue.

def promedio(lista):
    total = 0
    for n in lista:
        total += n
    return total/len(lista)

def mayorQue(lista, valor):
    for n in lista:
        if n > valor:
            print(n)

l = [1,2,3,4]
p = promedio(l)
print('El promedio es', p)
print('Los elementos de la lista mayores son')
mayorQue(l, p)

