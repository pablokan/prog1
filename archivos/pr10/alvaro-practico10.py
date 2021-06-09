class ObtenerMorosos():
    def __init__(self):
        self.lista = []
        op = ""
        while op != "3":
            print("\nMenú de Opciones")
            print("1- Carga")
            print("2- Resultado")
            print("3- Fin")
            op = input("Opción: ")

            if op == "1":
                print("\nSe han leido los datos") # cartel debería ir despues
                self.carga()
            elif op == "2":
                print("\nArchivo generado")
                self.graba()
        print("\nFin del programa")

    def carga(self):
        deudores = open("pr10/deudores.txt", "r")
        deudores.readline() #de esta forma el cursor va hasta el final y comienza en la otra linea
        lineas = deudores.readlines() 
        self.lista = []
        for li in lineas:
            self.lista.append(li.split(","))

    def graba(self):
        morosos = open("pr10/morosos-alvaro.txt","w")
        morosos.write("nombre - email - deuda\n")

        for e in self.lista:
            monto = e[4][1:e[4].find(".")]
            anio = e[5][6:]
            if int(monto) > 200000 and int(anio) == 2019:
                morosos.write(e[1] + " - ")
                morosos.write(e[2] + " - ")
                morosos.write(monto + "\n")

prueba1 = ObtenerMorosos()











    
