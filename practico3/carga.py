nombres = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 
'Campoamores, Susana', 'Santamaría, Carlos', 
'Skarsgard, Azul', 'Catalejos, Walter']
fechas = ['02/05/2012', '07/09/1984', '30/06/2003', 
'21/12/1967', '30/11/2003', '30/08/1995', '18/07/2018']

f = open('personas.txt', 'w')

for x in range(len(nombres)):
    grabar = nombres[x] + ' - ' + fechas[x] + '\n'
    f.write(grabar)

f.close()



