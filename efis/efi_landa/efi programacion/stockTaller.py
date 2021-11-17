import csv


class Equipo:
    def __init__(self, marca, modelo, dueno, problema):
        self.marca = marca
        self.modelo = modelo
        self.dueno = dueno
        self.problema = problema


class EquipoReparado(Equipo):
    def __init__(self, marca, modelo, dueno, problema, precio, fecha):
        Equipo.__init__(self, marca, modelo, dueno, problema)
        self.precio = precio
        self.fecha = fecha


class Operaciones:
    def __init__(self):
        self.listaSinReparar = []
        self.listaReparados = []
        self.listaEntregados = []

        archivo1 = open("equipoSinReparar.txt", "r")  # cambiar nombre archivo
        infoSR = csv.reader(archivo1, delimiter="&")

        archivo2 = open("equipoReparado.txt", "r")  # cambiar nombre archivo
        infoR = csv.reader(archivo2, delimiter="&")

        archivo3 = open("equipoEntregado.txt", "r")  # cambiar nombre archivo
        infoE = csv.reader(archivo3, delimiter="&")

        for x in infoSR:
            sinReparar = Equipo(x[0], x[1], x[2], x[3])
            self.listaSinReparar.append(sinReparar)

        for y in infoR:
            reparado = EquipoReparado(y[0], y[1], y[2], y[3], y[4], y[5])
            self.listaReparados.append(reparado)

        for z in infoE:
            entregado = EquipoReparado(z[0], z[1], z[2], z[3], z[4], z[5])
            self.listaEntregados.append(entregado)

        archivo1.close()
        archivo2.close()
        archivo3.close()

    def agregarEquipo(self):
        cond = "si"
        while cond == "si":
            print("EQUIPO A REPARAR")
            marca = input("marca: ")
            modelo = input("modelo: ")
            dueno = input("dueño: ")
            problema = input("problema: ")
            problema = problema + "\n"
            equip = Equipo(marca, modelo, dueno, problema)
            self.listaSinReparar.append(
                equip
            )  # terminar opcion de seguir cargando con validacion
            while cond == "si" or cond == "no":
                cond = input("desea agregar otro equipo(si/no)")
                if cond != "si" or cond != "no":
                    print("la opcion es incorrecta")

    def buscarEquipo(self, parametro):  # terminar print
        cont = 1
        for x in self.listaSinReparar:
            if parametro == x.marca:
                if x.marca.find(input("marca: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    cont += 1
                else:
                    print("no se encontro el equipo")
            elif parametro == x.modelo:
                if x.modelo.find(input("modelo: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    cont += 1
                else:
                    print("no se encontro el equipo")
            elif parametro == x.dueno:
                if x.dueno.find(input("dueño: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    cont += 1
                else:
                    print("no se encontro el equipo")

    def buscarEquipoReparado(self, lista, parametro):  # terminar print
        cont = 1
        for x in lista:
            if parametro == "marca":
                if x.marca.find(input("marca: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    print("   " + "precio: " + x.precio)
                    print("   " + "fecha: " + x.fecha)
                    cont += 1
                else:
                    print("no se encontro el equipo")
            elif parametro == "modelo":
                if x.modelo.find(input("modelo: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    print("   " + "precio: " + x.precio)
                    print("   " + "fecha: " + x.fecha)
                    cont += 1
                else:
                    print("no se encontro el equipo")
            elif parametro == "dueno":
                if x.dueno.find(input("dueño: ")) == 0:
                    num = str(cont)
                    print(num + ") " + "marca: " + x.marca)
                    print("   " + "modelo: " + x.modelo)
                    print("   " + "dueño: " + x.dueno)
                    print("   " + "problema: " + x.problema)
                    print("   " + "precio: " + x.precio)
                    print("   " + "fecha: " + x.fecha)
                    cont += 1
                else:
                    print("no se encontro el equipo")

    # def #selecciona 1 !!preguntar ¡¡

    def mostrarTodoEquipo(self):
        cont = 1
        for x in self.listaSinReparar:
            num = str(cont)
            print(num + ") " + "marca: " + x.marca)
            print("   " + "modelo: " + x.modelo)
            print("   " + "dueño: " + x.dueno)
            print("   " + "problema: " + x.problema)
            cont += 1

    def mostrarTodoEquipoReparado(self, lista):
        cont = 1
        for x in lista:
            num = str(cont)
            print(num + ") " + "marca: " + x.marca)
            print("   " + "modelo: " + x.modelo)
            print("   " + "dueño: " + x.dueno)
            print("   " + "problema: " + x.problema)
            print("   " + "precio: " + x.precio)
            print("   " + "fecha: " + x.fecha)
            cont += 1

    def mandarAReparado(self, indice):
        precio = input("precio: ")
        fecha = input("fecha: ")
        fecha = fecha + "\n"
        equi = self.listaSinReparar[indice]
        self.listaSinReparar.pop(indice)
        pro = equi.problema.strip("\n")
        equipo = EquipoReparado(equi.marca, equi.modelo, equi.dueno, pro, precio, fecha)
        self.listaReparados.append(equipo)

    def mandarAEntregado(self, indice):
        equi = self.listaReparados[indice]
        self.listaReparados.pop(indice)
        self.listaEntregados.append(equi)

    def grabarListas(self):
        archivo = open("equipoSinReparar.txt", "w")
        for equi in self.listaSinReparar:
            archivo.write(
                equi.marca + "&" + equi.modelo + "&" + equi.dueno + "&" + equi.problema
            )
        archivo.close

        archivo = open("equipoReparado.txt", "w")
        for equi in self.listaReparados:
            archivo.write(
                equi.marca
                + "&"
                + equi.modelo
                + "&"
                + equi.dueno
                + "&"
                + equi.problema
                + "&"
                + equi.precio
                + "&"
                + equi.fecha
            )
        archivo.close

        archivo = open("equipoEntregado.txt", "w")
        for equi in self.listaEntregados:
            archivo.write(
                equi.marca
                + "&"
                + equi.modelo
                + "&"
                + equi.dueno
                + "&"
                + equi.problema
                + "&"
                + equi.precio
                + "&"
                + equi.fecha
            )
        archivo.close


""" 
    equipo a reparar :agregar equipo :agrega
                                      atras

                      buscar equipo  :busca : muestra : selecciona 1 : mandar a reparado: agrega precio y fecha: cambia de txt
                                      atras             atras        : atras

                      mostrar todo   :        muestra : selecciona 1 : mandar a reparado: agrega precio y fecha: cambia de txt
                                                        atras        : atras
                      atras

    equipo reparado  :buscar equipo  :busca : muestra : selecciona 1 : mandar a entregado
                                      atras             atras          atras

                      mostrar todo   :        muestra : selecciona 1 : mandar a entregado
                                                        atras          atras
                      atras

    equipo entregado :buscar equipo  :busca : muestra : atras

                      mostrar todo   :        muestra : atras

                      atras

    salir
 """

if __name__ == "__main__":
    op = 0
    # declarar operacion 1 sola vez y borrar el resto
    while op != 4:
        print("presione el numero de lo operacion a realezar:")
        print("1) EQUIPO A REPARAR")
        print("2) EQUIPO REPARADO")
        print("3) EQUIPO ENTREGADO")
        print("4) SALIR")
        op = int(input("Ingrese opcion deseada: "))
        if op == 1:  # equipo a reparar
            operaReparar = 0
            while operaReparar != 4:
                print("EQUIPO A REPARAR")
                print("presione el numero de lo operacion a realezar:")
                print("1) Agregar equipo")
                print("2) Buscar equipo")
                print("3) Mostrar todo")
                print("4) Atras")
                operaReparar = int(input("Ingrese opcion deseada: "))
                if operaReparar == 1:
                    operacion = Operaciones()
                    operacion.agregarEquipo()
                    operacion.grabarListas()
                elif operaReparar == 2:
                    operacion = Operaciones()
                    opcion = 0
                    while opcion != 4:
                        print("EQUIPO A REPARAR")
                        print("presione el numero de lo operacion a realezar:")
                        print("Buscar por:")
                        print("1) Marca")
                        print("2) Modelo")
                        print("3) Dueño")
                        print("4) Atras")
                        opcion = int(input("Ingrese opcion deseada: "))
                        if opcion == 1:
                            param = "marca"
                        elif opcion == 2:
                            param = "modelo"
                        elif opcion == 3:
                            param = "dueno"
                        elif opcion == 4:
                            param = ""
                        else:
                            print("la opcion es incorrecta")
                    operacion.buscarEquipo(param)
                    # seleccionar 1 o atras
                    # mandar a reparado
                    # cambiar lista
                    operacion.grabarListas()
                elif operaReparar == 3:
                    operacion = Operaciones()
                    print("EQUIPO A REPARAR")
                    operacion.mostrarTodoEquipo()
                    # seleccionar 1 o atras
                    # cambiar lista
                    operacion.grabarListas()
                elif operaReparar == 4:
                    operacion = Operaciones()
                    operacion.grabarListas()
                else:
                    print("la opcion es incorrecta")
        elif op == 2:  # equipo reparado
            operaReparado = 0
            while operaReparado != 4:
                print("EQUIPO REPARADO")
                print("presione el numero de lo operacion a realezar:")
                print("1) Buscar equipo")
                print("2) Mostrar todo")
                print("3) Atras")
                operaReparado = int(input("Ingrese opcion deseada: "))
                if operaReparado == 1:
                    operacion = Operaciones()
                    print("EQUIPO REPARADO")
                    print("presione el numero de lo operacion a realezar:")
                    print("Buscar por:")
                    print("1) Marca")
                    print("2) Modelo")
                    print("3) Dueño")
                    print("4) Atras")
                    opcion = int(input("Ingrese opcion deseada: "))
                    if opcion == 1:
                        param = "marca"
                    elif opcion == 2:
                        param = "modelo"
                    elif opcion == 3:
                        param = "dueno"
                    elif opcion == 4:
                        param = ""
                    else:
                        print("la opcion es incorrecta")
                    operacion.buscarEquipoReparado(self.listaReparados, param)
                    # seleccionar 1 o atras
                    # cambiar lista
                    operacion.grabarListas()
                elif operaReparado == 2:
                    operacion = Operaciones()
                    print("EQUIPO REPARADO")
                    operacion.mostrarTodoEquipoReparado(self.listaReparados)
                    # seleccionar 1 o atras
                    operacion.grabarListas()
                elif operaReparado == 3:
                    operacion = Operaciones()
                    operacion.grabarListas()
                else:
                    print("la opcion es incorrecta")
        elif op == 3:  # equipo entregado
            operaEntregado = 0
            while operaEntregado != 4:
                print("EQUIPO ENTREGADO")
                print("presione el numero de lo operacion a realezar:")
                print("1) Buscar equipo")
                print("2) Mostrar todo")
                print("3) Atras")
                operaReparado = int(input("Ingrese opcion deseada: "))
                if operaEntregado == 1:
                    operacion = Operaciones()
                    print("EQUIPO ENTREGADO")
                    print("presione el numero de lo operacion a realezar:")
                    print("Buscar por:")
                    print("1) Marca")
                    print("2) Modelo")
                    print("3) Dueño")
                    print("4) Atras")
                    opcion = int(input("Ingrese opcion deseada: "))
                    if opcion == 1:
                        param = "marca"
                    elif opcion == 2:
                        param = "modelo"
                    elif opcion == 3:
                        param = "dueno"
                    elif opcion == 4:
                        param = ""
                    else:
                        print("la opcion es incorrecta")
                    operacion.buscarEquipoReparado(self.listaEntregados, param)
                    # seleccionar 1 o atras
                    # cambiar lista
                    operacion.grabarListas()
                elif operaEntregado == 2:
                    operacion = Operaciones()
                    print("EQUIPO ENTREGADO")
                    operacion.mostrarTodoEquipoReparado(self.listaEntregados)
                    # seleccionar 1 o atras
                    operacion.grabarListas()
                elif operaEntregado == 3:
                    operacion = Operaciones()
                    operacion.grabarListas()
                else:
                    print("lo opcion es incorrecta")
        elif op == 4:  # salir
            operacion = Operaciones()
            operacion.grabarListas()
        else:
            print("la opcion es incorrecta")
