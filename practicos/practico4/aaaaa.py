todo = [
'1,Veriee,vvasilkov0@qq.com,Female,$374324.12,09/04/2020,Besançon',
'2,Lizbeth,locklin1@tiny.cc,Female,$423222.26,14/09/2019,Jawand',
'3,Tymon,thillum2@diigo.com,Male,$591323.65,08/01/2020,Rîbniţa'
]

for linea in todo:
    print('esto es linea ---->', linea)
    persona = linea.split(',')
    print(persona)
    nombre = persona[1]
    mail = persona[2]
    saldo = persona[4][1:-3]
    anio = persona[5][-4:]
    print(anio)
    





    





