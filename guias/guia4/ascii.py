def aMayuscula(palabra):
    mayuscula = ""
    for letra in palabra:
        ordMay = ord(letra)-32
        mayuscula += chr(ordMay)
    return mayuscula


p = input('ingrese una palabra en minúscula: ')
print(aMayuscula(p))
print(aMayuscula('aprendizaje'))
print(aMayuscula('campeonato'))







