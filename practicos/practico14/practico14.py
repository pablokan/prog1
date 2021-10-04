class Empleado():
    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

      

class Programador(Empleado):
    def __init__(self, lang):
        self.lang = lang

    def setProject(self, project):
        self.project = project

    def getData(self):
        return self.lang, self.project


class Empresa():
    def __init__(self, nombre, rubro):
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []
        self.nombre = nombre
        self.rubro = rubro

    def getInfo(self):
        return self.nombre, self.rubro

    def addEmp(self):
        lang = input("Lenguaje: ")
        if lang in self.listaLenguajes:
            p = Programador(lang)
            n = input("Nombre: ")
            p.setName(n)
            if lang == "Python":
                sal = 125000
            else:
                sal = 75000
            p.setSalary(sal)
            print("Proyecto:", self.listaProyectos)
            op = input("Elija 1 o 2: ")
            p.setProject(self.listaProyectos[int(op)-1])
            self.listaProgramadores.append(p)
        else:
            print("lenguajes pedidos:", self.listaLenguajes)

    def mostrarTodo(self):
        nE, ru = self.getInfo()
        print(nE, ru)
        for e in self.listaProgramadores:
            l, p = e.getData()
            print(e.getName(), e.getSalary(), "Lenguaje:", l, " Proyecto:", p)


class App():
    def __init__(self, cE):
        empresa = Empresa("itecLabs", "Desarrollo de Software")
        for i in range(cE):
            empresa.addEmp()
        empresa.mostrarTodo()

app = App(4)    


















