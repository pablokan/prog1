class App():
    def __init__(self):
        nombres = ["Darby", "Hugh", "Estel", "Haze","Delphinia", "Chet"]
        fechas = ["26/11/2006", "16/04/1996", "10/04/2012", "05/09/2016", "23/02/1996", "18/02/2014"]
        a = open("personas.txt", "w")
        for i in range(len(nombres)):
            nombre = nombres[i]
            fecha = fechas[i]
            linea = nombre + " -*- " + fecha + "\n"
            a.write(linea)
        a.close()

    def opera(self):
        a = open("personas.txt", "r")
        b = open("mayores.txt", "w")
        todo = a.readlines()
        for li in todo:
            posFecha = li.find("-*-") + 4
            fecha = li[posFecha:-1]
            dia = int(fecha[:2])
            mes = int(fecha[3:5])
            ani = int(fecha[6:])

            edad = 2020 - ani
            if mes > 8 or mes == 8 and dia > 24:
                edad -= 1

            if edad >= 18:
                b.write(li[:posFecha-5] + "\n")
                
app = App()
app.opera()

