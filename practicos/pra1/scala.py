nombres_completos = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
sexos = ['f', 'f', 'm', 'f', 'm', 'f', 'm']
fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']
nombres = ['Ana', 'Kate', 'Benicio', 'Susana', 'Carlos', 'Azul', 'Walter']

################################################

#print("Iniciales y apellido de las personas:")
################################################
def armarLista(cadena):
    d = ''
    for l in cadena:
        if l not in ',.':
            d += l
    return d.split(' ')

def masLarga(lista):
    c = 0
    for palabra in lista:
        if len(palabra) > c:
            c = len(palabra)
    return c
    
c1 = 0
for i in nombres:
    x1 = masLarga(armarLista(i))

    if x1 > c1:
        c1 = x1
        nom = nombres[i]

print("El nombre mas largo es: ", nom)
################################################
from calcula_edad import edad



#print("El promedio de edad de las mujeres es: ", )