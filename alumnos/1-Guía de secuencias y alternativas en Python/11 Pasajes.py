import os
os.system('cls')
Costo = 1700
Nombre = input('Ingrese nombre del pasajero: ' )
Edad = int(input('Ingrese la edad del pasajero: '))
if Edad>65:
    print('Estimado ', Nombre, 'el valor de su pasaje es: $ ', Costo*0.6)
elif Edad<10 and Edad>5:
    print('Estimado ', Nombre, 'el valor de su pasaje es: $ ', Costo*0.60)
else:
    print('Estimado ', Nombre, 'el valor de su pasaje es: $ ', Costo)
