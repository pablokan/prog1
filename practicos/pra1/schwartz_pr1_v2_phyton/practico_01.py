nombre_completo= ['Torres, Ana','Hudson, Kate','Quesada, Benicio','Campoamores, Susana','Santamaría, Carlos ','Skarsgard, Azul','Catalejos, Walter']
sexo=['f','f','m','f','m','f','m']
fecha_nacimiento=['02/05/1943','07/09/1984','10/02/1971','21/12/1967','30/01/1982','30/08/1995','18/07/1959']

#1) Mostrar las iniciales de los nombres con apellido completo de todas las personas.

str_nombre_completo=(','.join(nombre_completo)).split('[]' and ',') 

solonombres=[]
apellidos=[]
for i in range(len(str_nombre_completo)):
    if i %2 ==0 :
        

        apellidos.append(str_nombre_completo[i])
    elif (i+1) %2 ==0 :
        
        solonombres.append(str_nombre_completo[i])

primer_letra= []
for i in solonombres:
   primer_letra += i[1]


for l, j in zip(primer_letra, apellidos):
    print(l,'.',j)



#2) Decir cual es el nombre de pila más largo.
print('El nombre mas largo es: ', max(solonombres, key=len))


#3) Mostrar el promedio de edad de las mujeres. (Pueden usar la función edad del módulo calcula_edad
#que está subida en el Classroom)

from calcula_edad import edad


mujeres=[]
edades_mujeres=[]
nacimientos_mujeres=[]
acum=0
for m in range (len(nombre_completo)):
    if sexo[m] == 'f':
        mujeres.append(nombre_completo[m]) 
        nacimientos_mujeres.append(fecha_nacimiento[m])
        edades_mujeres.append(edad(fecha_nacimiento[m]))

for m in (edades_mujeres):
     acum += m
print('El promedio de edad de las mujeres es:  ' ,int( acum/(len(mujeres))))