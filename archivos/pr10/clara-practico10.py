class App():
    def __init__(self):
        op = ""
        while op != 3:
            print("\nMenú de Opciones")
            print("1- Carga")
            print("2- Resultado")
            print("3- Fin")
            op = int(input("Opción: "))

            if op == 1:
                self.carga()
            elif op == 2:
                self.grabar()
        print("Bye")
        
    def carga(self):
        a = open("pr10/deudores.txt", "r",encoding="utf8")
        listas = a.readlines()
        self.listas = a.readlines()
        a.close()
        self.lista = []
        for i in range(len(listas)):
            listaa = listas[i].split(",")
            self.lista.append(listaa)
        self.lista.pop(0)


    def grabar(self):
        nombre =[]
        mail = []
        sexo = []
        deuda = []
        fecha = []
        for i in range(len(self.lista)):
            nombre.append(self.lista[i][1])
            mail.append(self.lista[i][2])
            sexo.append(self.lista[i][3])
            deuda.append(int(self.lista[i][4][1:-3]))
            fecha.append(int(self.lista[i][5][6:]))

        deuda200000=[]
        a = open("pr10/morososclara.txt", "w")
        a.write("Nombre, mail, deuda\n")
        for i in range(len(deuda)):
            if (deuda[i] > 200000) and(fecha[i]==2019):
                dato = i,nombre[i],mail[i],deuda[i]
                datos = nombre[i]
                datos1 = mail[i]
                datos2 = str(deuda[i])
                deuda200000.append(dato)
                a.write(datos)
                a.write(", ")
                a.write(datos1)
                a.write(", ")
                a.write(datos2)
                a.write("\n")

        a.close()
        print(deuda200000)


f = App()
f.carga
f.grabar