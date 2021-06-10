# 11. Ingresar la lluvia caída en milímetros 
# para cada día de la semana. 
# Mostrar al final el total de lluvia caída y 
# el nombre del día que más llovió.

from dob_val_func import inputNumber

# def main():
#     dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
#     print('Lluvia caída en la semana')
#     total = 0
#     mas = 0
#     for d in dias:
#         mensaje = 'Día ' + d + ': '
#         ll = inputNumber("entero", mensaje)
#         if ll > mas:
#             mas = ll
#             humedo = d
#         total += ll
#     print(total, humedo)

# main()


semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

def carga():
    lista = []
    print('Lluvia caída en la semana')
    for d in semana:
        mensaje = 'Día ' + d + ': '
        ll = inputNumber("entero", mensaje)
        lista.append(ll)
    return lista

def total(lista):
    t = 0
    for e in lista:
        t += e
    return t

def diaQueMasLlovio(lista, dias):
    masLLuvia = 0
    diaMasLluvioso = ''
    for x in range(len(lista)):
        if lista[x] > masLLuvia:
            masLLuvia = lista[x]
            diaMasLluvioso = dias[x]
    return diaMasLluvioso

listaMM = carga()
print('Total lluvia caída:', total(listaMM))
print(diaQueMasLlovio(listaMM, semana))

    










