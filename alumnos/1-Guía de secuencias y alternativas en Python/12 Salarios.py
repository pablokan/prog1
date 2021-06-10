import os
os.system('cls')
from datetime import date
Empleado = input('Nombre del empleado: ')
Diaing = int(input('Día de ingreso: '))
Mesing = int(input('Mes de ingreso: '))
Anoing = int(input('Año de ingreso: '))
Faltado = int(input('Dias ausentes: '))
Aniohoy = date.today().year
Meshoy = date.today().month
Diahoy = date.today().day
Antig = Aniohoy - Anoing
Sueldo = (47000)
SueAntig = int(Sueldo*1.3)
if Faltado>0:
    print('El sr. {}, registra ausentes'.format(Empleado))
    print('El Sueldo del sr. {}, es $ {}'.format(Empleado, Sueldo))
elif Antig>5:
    print('La antigüedad del sr. {}, es de mas de 5 años'.format(Empleado))
    print('El Sueldo del sr. {}, es $ {}'.format(Empleado, SueAntig))
else:
    print('El Sueldo del sr. {}, es $ {}'.format(Empleado, Sueldo))

    

