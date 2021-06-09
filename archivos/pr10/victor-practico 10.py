#>>>Victor Andres Barilin<<<
class App():
    def __init__(self):
        op = 0
        while op != 2:
            print ("_")
            print ("1- Cargar")
            print ('2- Salir')
            op = int(input("Elija una opción (1 o 2)"))
            if op == 1:
                self.carga()
            elif op == 2:
                print('-----------------------------')
                print('Gracias por usar este sistema')
                print('-----------------------------')

    def carga(self):
        deuda = []
        listDeud = open("pr10/deudores.txt", "r")
        todo = listDeud.readlines()
        print(len(todo), "líneas leídas")
        listDeud.close()
        New = open('pr10/victor-morosos.txt', 'w')
        c = 0
        for x in todo:
            if '/2019' in x:
                aux = x.find("$")
                aux2 = x.find (".",aux)
                deuda = int(x[(aux+1):aux2])
                if  deuda >= 200000:
                    c += 1
                    if c == 1:
                        New.write('id - nombre - email - deuda\n')
                    nom = x.find(',')
                    nomF = x.find(',',(nom + 1))
                    name = x[(nom + 1) : nomF]
                    mai = x.find(',',(nomF + 1))
                    mail = x[nomF + 1 : mai]
                    New.write(str(c)+'-'+ name + '-'+ mail +'-'+ str(deuda) + '\n')
        New.close()
App()