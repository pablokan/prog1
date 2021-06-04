nombres="Torres, Ana;Hudson, Kate;Quesada, Benicio;Campoamores, Susana;Santamaría, Carlos;Skarsgard, Azul;Catalejos, Walter"
sexo=["f","f","m","f","m","f","m"]
fechanac =["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
#parte1-----------------------------------------------------------------
inicial='A. '+ nombres[:6]
print(inicial)
inicial2='K. '+nombres[12:18]
print(inicial2)
inicial3='B. '+nombres[25:32]
print(inicial3)
inicial4='S. '+nombres[42:53]
print(inicial4)
inicial5='C. '+nombres[62:72]
print(inicial5)
inicial6='A. '+nombres[81:90]
print(inicial6)
inicial7='W. '+nombres[97:106]
print (inicial7)

#parte 2-----------------------------------------------------------------
separadores = (';')

for x in range(len(separadores)):
    nombres = nombres.replace(separadores[x], ' ')

nombres2 = nombres.split()

p1 = len(nombres2[0]) 
p2 = len(nombres2[1]) 
p3 = len(nombres2[2]) 
p4 = len(nombres2[3])
p5 = len(nombres2[4])

print('el nombre mas largo es: ', nombres2[5],"y tiene",p3,"letras")

#parte 3-----------------------------------------------------------------
from calcula_edad import edad
fechanac =["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
sexo=["f","f","m","f","m","f","m"]

if __name__ == '__main__':
    edadmuj1=int(edad('02-05-1943'))
    edadmuj2=int(edad('07-09-1984'))
    edadmuj3=int(edad('21-12-1967'))
    edadmuj4=int(edad('30-08-1995'))

cantmuj = 0 
for x in range(len(sexo)):
    if sexo[x] == "f":
        cantmuj= cantmuj + 1


edadtotalmuj = edadmuj1 + edadmuj2 + edadmuj3 + edadmuj4 
edadpromediomuj=edadtotalmuj / cantmuj
print("el promedio de edad de las mujeres es de:",int(edadpromediomuj))







