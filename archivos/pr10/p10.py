class App():
    
    def __init__(self):
        op = ""
        while op != "3": 
            print("\nMenú de Opciones")
            print("1- Carga")
            print("2- Grabar nuevo archivo")
            print("3- Salir")
            op = input("Opción: ")

            if op == "1":
                self.carga()
            elif op == "2":
                self.graba()
        print("Bye")

    def carga(self):
        a = open('pr10/deudores.txt', 'r')
        cabecera = a.readline()
        self.lineasLeidas = a.readlines()
        print(len(self.lineasLeidas), "líneas leídas")
        a.close()

    
    def graba(self):
        a = open('pr10/morosos.txt', 'w')
        cabecera = "Nombre,Mail,Saldo"
        a.write(cabecera + "\n")
        c = 0
        lineasGrabar = []
        for li in self.lineasLeidas:
            if "/2019" in li:
                lis = li.split(",")
                saldo = int(lis[4][1:-3])
                if  saldo > 200000:
                    lineaNueva = lis[1] + " - " + lis[2] + " - " + str(saldo) + "\n"
                    lineasGrabar.append(lineaNueva)
                    c += 1
        a.writelines(lineasGrabar)
        print(c, "líneas grabadas")
        a.close()


app = App()
