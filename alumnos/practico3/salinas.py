def inputPeople(Nombres,Apellido):
    Nomb = []
    Apell = []
    
    for i in range(6):
        Nombres = input('ingresar un nombre: ')
        Nomb.append(Nombres)
        Apellido = input('ingresar un apellido: ')
        Apell.append(Apellido)
        

    return Nomb, Apell, 
Nombres, Apellido, = inputPeople('ingresar un nombre','ingresar el apellido:')      

file = open('Tp3.txt','w')
file.write = Nombres == Nombres
file.write = Apellido == Apellido

file = open('Tp3.txt','r')
all = file.read()
print(all)
file.close()

acumulador = int(0)
for i in range(1,7):
     edad =  int(input('ingresar la edad: '));
     acumulador = acumulador + edad;
     
print('los mayores de edad son: ', str(acumulador / 20)); 


















