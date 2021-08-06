from datetime import date
from input_int import inputInt

def main():
    def stop():
        input('Enter para volver al menú')

    def carga():
        archivo = open("todo_list.txt", "r")
        titulos = archivo.readline().split(",")
        print('Títulos', titulos)
        lista = []
        for linea in archivo:
            lista.append(linea[:-1].split(","))
        archivo.close()
        return titulos, lista

    def agregar():
        pass

    def listar():
        print(titulos, lista)
        stop()

    def urgente():
        for i in range(len(lista)):
            if lista[i][2] == 'True':
                print(lista[i])
        stop()

    def hoy():
        for i in range(len(lista)):
            if lista[i][3] == date.today().isoformat():
                print(lista[i])
        stop()

    def menu():
        op = 0
        while op != 5:
            print('1. Agregar')
            print('2. Todos')
            print('3. Urgente')
            print('4. Hoy')
            print('5. Salir')
            op = inputInt('Opción: ', min=1, max=5)
            if op == 1:
                agregar()
            elif op == 2:
                listar()
            elif op == 3:
                urgente()
            elif op == 4:
                hoy()
            elif op == 5:
                print('Adiós')

    titulos, lista = carga()
    menu()

if __name__ == '__main__':
    main()
