#Necesitamos saber el nombre, la dirección de correo y el saldo de todos los que deben más 
#de doscientos mil pesos y cuya deuda sea del año pasado.
abrir=open("deudores.txt","r",encoding="utf-8")
listad=abrir.read()
listaseparada=listad.split(",")
nombres=listaseparada[7::6]
email=listaseparada[8::6]
genero=listaseparada[9::6]
deuda=listaseparada[10::6]
fecha=listaseparada[11::6]
ciudad=listaseparada[12::6]

deudanumeros=[]
for p in deuda:
    deuda1 = int(p[1:-3])
    deudanumeros.append(deuda1)

añodueda=[]
for p in fecha:
    fecha1 = int(p[6:])
    añodueda.append(fecha1)

morosos=open("morosos.txt","w")
morosos.write("nombre,email,deuda\n")

for i in range(len(deudanumeros)):
    if deudanumeros[i]>200000 and añodueda[i]<=2019:
        morosos.write('%s,' % nombres[i])
        morosos.write('%s,' % email[i])
        morosos.write('%s\n' % deudanumeros[i])
morosos.close()
    

