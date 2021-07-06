def inputChoice(listaOpc, mensaje='Elija una opción'):
    listaOpc = listaOpc.split('//')
    concOp = ' '
    for op in listaOpc:
        concOp += op
        mensaje = mensaje + ' => ' + concOp
    print(mensaje)
    a = input()
    return a

if __name__=='__main__':
    q = inputChoice('si//no//no sé')
    print(q)
