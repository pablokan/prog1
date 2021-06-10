# 1: Pedir el ingreso de 10 números. Contar los mayores de 23. Almacenar los que cumplen la condición

c=0
i=1
list23=[]
while i<=10:
    num=int(input('Ingrese un número: '))
    if num>23:
        c=c+1
        list23.append(num)
    i=i+1    

# 2: Mostrar el resultado.
print('Eso fué todo, ingresó ', c, ' mayores que 23, y fueron: ')
print(list23)