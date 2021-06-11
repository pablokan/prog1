
nombre = []
fechas = []

def carga ():
    respuesta = (input('desea ingresar algun nombre?:'))
    texto = open('name.txt','w')
    while respuesta == 'si' or respuesta == 'SI' or respuesta == 'Si' or respuesta == 'sI' :
        
        nom = (input('ingrese su nombre:'))
        nom = nom + ','
        nombre.append(nom)
        
        fe = (input('ingrese su fecha de nacimiento:'))
        fe = fe + ','
        fechas.append(fe)
        respuesta = (input('desea ingresar algun otro nombre?:'))
        
        
    texto.writelines(nombre)
    texto.writelines("\n")
    texto.writelines(fechas)
    texto.close()

respuesta = carga()

