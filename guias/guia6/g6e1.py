def conca(*args, caracter=' '):
    for p in args:
        d = caracter.join(args)
    return d

print(conca('hola', 'chau', 'nos vemos', 'otro dia', caracter="*-*"))
