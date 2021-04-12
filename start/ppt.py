ganador = ''
eleccionComputadora = 'piedra'
eleccionUsuario = input('piedra, papel o tijera? ')

if eleccionComputadora == eleccionUsuario:
    ganador = 'Empate'
elif eleccionComputadora == 'papel' and eleccionUsuario == 'piedra':
    ganador = 'Computadora'
elif eleccionComputadora == 'piedra' and eleccionUsuario == 'tijera':
    ganador = 'Computadora'
elif eleccionComputadora == 'tijera' and eleccionUsuario == 'papel':
    ganador = 'Computadora'
else:
    ganador = 'Usuario'
    
if ganador == 'Empate':
    print('Ambos eligieron', eleccionComputadora)
else:
    print(ganador, 'ganó. La computadora eligió', eleccionComputadora + '.')
