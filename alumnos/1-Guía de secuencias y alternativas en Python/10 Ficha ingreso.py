import os
os.system('cls')
Nombre = input('Ingrese su Nombre: ')
Carrera = input('Ingresante a: ')
Ciudad = input('Su ciudad es: ')
Cuota = 4500
print('Sr. ', Nombre, 'Confirmamos su solicitud de inscripción en ', Carrera)
if Carrera=='Electromecánica':
    if Ciudad=='Río Cuarto':
       print('Su cuota final será de $ 4.500.-')
    else:
        print('Por no ser residente en Río Cuarto y cursar Electromecánica, accede a un descuento del 15%. Su cuota final será de $ ', Cuota*0.85)
else:
    print('Su cuota final será de $ 4.500.-')
print('Sr. {}, de la ciudad de {}, queda inscripto en la carrera de {}'.format(Nombre, Ciudad, Carrera))

