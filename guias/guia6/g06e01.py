def concate(*args, caracter=' '):
    return caracter.join(args)

if __name__ == '__main__':
    print(concate('hola', 'chau'))
    print(concate('hola', 'chau', caracter='+'))
    print(concate('hola', 'como va todo?', 'chau', caracter='/'))


