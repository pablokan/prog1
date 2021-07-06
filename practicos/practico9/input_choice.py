def inputChoice(listaOpc, mensaje='Elija una opción'):
    mensaje = mensaje + ' (' + listaOpc + '): '
    listaOpc = listaOpc.split('/')
    op = ''
    while op not in listaOpc:
        op = input(mensaje)
    return op

if __name__=='__main__':
    q = inputChoice('si/no/a veces')
    print(q)
    r = inputChoice('rojo/verde', 'Elija un color')
    print(r)
    