def carga():
    nombres = []
    fechas = []
    respuesta = str(input("Quiere ingresar algun nombre? "))
    t = open('nyf.txt','w')
    while respuesta == "Si" or respuesta == "si":
        nombre = str(input("Ingrese un nombre: "))
        nombre = nombre + ','
        nombres.append(nombre)
        
        fecha = str(input("Ingrese la fecha correspondiente: "))
        fecha = fecha + ','
        fechas.append(fecha)
        
        respuesta = str(input("Quiere ingresar otro nombre? "))
    t.writelines(nombres)
    t.writelines('\n')
    t.writelines(fechas)
    t.close()
respuesta = carga()