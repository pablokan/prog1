import csv

archivo1 = open("equipoSinReparar.txt","r")# cambiar nombre archivo
infoSR =  csv.reader(archivo1, delimiter="&")
        
archivo2 = open("equipoReparado.txt","r")# cambiar nombre archivo
infoR =  csv.reader(archivo2, delimiter="&")

archivo3 = open("equipoEntregado.txt","r")# cambiar nombre archivo
infoE =  csv.reader(archivo3, delimiter="&")

cont1=0
for x in infoSR:
    cont1 += 1
    print(cont1 , "-" , x)

cont2 =0
for y in infoR:
    op = 0
    cont2 += 1
    print(cont2 , "-" , y)
    for a in y:
        op += 1
        print(op)
cont3 =0
for z in infoE:
    cont3 += 1
    print(cont3 , "-" , z)

archivo1.close()
archivo2.close()
archivo3.close()