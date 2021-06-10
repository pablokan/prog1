import os
os.system('cls')
Primero = int(input('Escriba un número par........'))
Segundo = int(input('Escriba otro número, pero ahora que sea impar......'))
Tercero = '+'
Cuarto = '-'
Quinto = input('Elija una de las dos funciones matematicas basicas, + o -.....')
if Quinto==Tercero:
    print(Primero + Segundo)
else:
    print(Primero - Segundo)
