listaNombre = ['Torres, Ana','Hudson, Kate','Quesada, Benicio','Campoamores, Susana','Santamaría, Carlos','Skarsgard, Azul ','Catalejos, Walter']
listaGenero = ['f','f','m','f','m','f','m']
listaFechaDeNacimiento = ['02/05/1943','07/09/1984','10/02/1971','21/12/1967','30/01/1982','30/08/1995','18/07/1959']
elSiguienteDe= ' '

#1) Mostrar las iniciales de los nombres con apellido completo de todas las personas.
posicion = 0
letra = ''
listaInicilales= []
apellido = ''
for i in range(len(listaNombre)):
    posicion = listaNombre[i].find(elSiguienteDe)
    letra = listaNombre[i][posicion+1]
    listaInicilales.append(letra)
    apellido= listaNombre[i][:posicion]
    listaInicilales[i] = listaInicilales[i] + '. '+ apellido 

#MODULO PARA MOSTRAR EN PANTALLA LA LISTA
print('Iniciales y apellido de las personas:')
ntexto= ''
for i in listaInicilales:
    if i not in ',':
        ntexto += i
print(ntexto)
textofinal= ntexto.split(',')
for i in textofinal:
    print(i)

#2) Decir cual es el nombre de pila más largo.

largo=0
NombreMayor= ''
listaSoloNombre = []
for i in range (len(listaNombre)):
    posicion = listaNombre[i].find(elSiguienteDe)
    soloNombre= listaNombre[i][posicion+1:]
    listaSoloNombre.append(soloNombre)
    largoNombre = len(soloNombre)
    if largoNombre > largo:
        largo = largoNombre
        NombreMayor = listaSoloNombre[i]
print('El nombre mas largo es:', NombreMayor,'\n')

#3) Mostrar el promedio de edad de las mujeres. (Pueden usar la función edad del 
# módulo calcula_edad que está subida en el Classroom)

from calcula_edad import edad  
acu =0
for x in range(len(listaNombre)):
    acu+= edad(listaFechaDeNacimiento[x]) 
promedio=acu// (len(listaFechaDeNacimiento))
print('El promedio de edad de las mujeres es: ',promedio,'\n')



