nya = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 
'Santamaria, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter' ] 
fecNac = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']
sexos = ['f', 'f','m', 'f', 'm', 'f','m']
edades = [78, 37, 50, 54, 39, 26, 62]

nombres = []
apellidos = []

#eliminar coma de la lista Nombres
for i in range(len(nya)):
    posC = nya[i].find(',')
    nombres.append(nya[i][posC+2:])
    apellidos.append(nya[i][:posC])
print (nombres)

#Mostrar las iniciales de los nombres con apellido completo
for i in range(len(nombres)):
    suprN = nombres[i][0] + '.' + apellidos[i]
    print (suprN)

#Nombre mas largo
masLetras = 0
nombreMasLargo = ''
for i in range(len(nombres)):
    if len(nombres[i]) > masLetras:
        masLetras = len(nombres[i])
        nombreMasLargo = nombres[i]
print (nombreMasLargo, masLetras)

# El promedio de edad de las mujeres
SumaEdM = 0
contM = 0
for i in range(len(edades)):
    if sexos[i] == 'f':
        SumaEdM += edades[i]
        contM += 1
print ('promedio edad mujeres: ', SumaEdM / contM)
