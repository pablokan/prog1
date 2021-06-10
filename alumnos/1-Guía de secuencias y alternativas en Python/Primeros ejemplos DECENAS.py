import os
os.system('cls')
num = input('Ingrese un numero natural (entero positivo)')
num = int(num)
if num<10:
    print('Primera decena')
if num>=10 and num<20:
    print('Segunda decena')
if num>=20 and num<30:
    print('Tercera decena')
else:
    print('30 o mas')
