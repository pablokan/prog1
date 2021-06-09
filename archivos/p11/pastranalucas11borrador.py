class InfoPelis():

    def setTitulos(self):
        multiplos = [1] #9       
        cantidad = 3
        nombretitulos = []
        x = 1 #9
        for i in range(1,cantidad):
            x += 32
            multiplos.append(x)  
        archPelis = open("pelis.json", "r")    
        cantidadDP = 0
        x = "nada"
        while x != "":
            caracter = archPelis.read(1)
            if caracter == ":":
                cantidadDP += 1
                for e in multiplos:
                    tituloInicio = ""
                    if e == cantidadDP:
                        archPelis.seek(archPelis.tell()+2)
                        n = archPelis.read(1)
                        while n !='"': #','
                            tituloInicio += n
                            n = archPelis.read(1)
                            if n == '"': #','
                                nombretitulos.append(tituloInicio)
                                print(nombretitulos)
        archPelis.close()

    def setActores(self):
        multiplos = [9]       
        cantidad = 3
        nombreActores = []
        x = 9
        for i in range(1,cantidad):
            x += 32
            multiplos.append(x)  
        archPelis = open("pelis.json", "r")    
        cantidadDP = 0
        x = "nada"
        while x != "":
            caracter = archPelis.read(1)
            if caracter == ":":
                cantidadDP += 1
                for e in multiplos:
                    actorInicio = ""
                    if e == cantidadDP:
                        archPelis.seek(archPelis.tell()+2)
                        n = archPelis.read(1)
                        while n !=',': 
                            actorInicio += n
                            n = archPelis.read(1)
                            if n == ',': 
                                nombreActores.append(actorInicio)
                                print(nombreActores)
        archPelis.close()

    
prog = InfoPelis()
prog.setActores()
prog.setTitulos()

