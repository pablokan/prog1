from datetime import date
def inputDate(mensaje):
    valido = False
    d = ""
    while not valido:
        d = input(mensaje)
        try:
            f = date(int(d[6:]), int(d[3:5]), int(d[:2]))
            valido = True
        except:
            print('ingreso erróneo')
    return int(d[6:]), int(d[3:5]), int(d[:2])

if __name__ == '__main__':
    a, m, d = inputDate('Ingrese fecha de nacimiento: ')
    print(a, m, d)

