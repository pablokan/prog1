apellido_nombre=["Torres, Ana","Hudson, Kate","Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul" ,"Catalejos, Walter" ]
sexo=["f","f","m","f","m","f","m"]
fecha_de_nacimiento=["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
nombres_apellidos="-".join(apellido_nombre)
print(nombres_apellidos)
aux=[]
for i in range (len(apellido_nombre)):
    comas= apellido_nombre[i].find(",")
    nombres= apellido_nombre[i][comas+2]
    apellidos= apellido_nombre[i][:comas]
    IncialNombre= nombres[0]
    aux.append(IncialNombre +"."+ apellidos)
print ("inciales y apellidos de las siguientes personas:",)
for i in range (len(apellido_nombre)):
     print(aux[i])
# ACTIVIDAD 2 :Buscar el nombre mas largo
nuevalista=[]
cont= 0
i=""
for i in range (len(apellido_nombre)):
     nombre= apellido_nombre[i].find(",")
     nombre2= apellido_nombre[i][nombre+2:]
     nuevalista.append(nombre2)
for i in range(len(apellido_nombre)):
    o =(len(nuevalista[i]))
    if o > cont:
        cont = o
        nombremaslargo = nuevalista[i]
print("El nombre mas largo es:",nombremaslargo)
 




