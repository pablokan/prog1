from lib_valid.funcion_validar import inputNumber

nombre = input('Nombre: ')
edad = inputNumber('entero', 'Edad: ')
altura = inputNumber('real', 'Altura: ')

print('Hola', nombre, 'tenés', edad, 'años y medís', altura)
