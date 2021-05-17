from random import randint
sPalabras = 'lapicera cuaderno tetera barco aguja tijera esmalte piedra cerdo cebra cepillo sierra carro tinta cinta peine gancho cierre valija cuerda radio televisor mueble soldado plato jarra tigre suelo viento lluvia fuego abanico abastecimiento abeja abstinencia abuela abundancia caudillo director harina trigo bandeja calentador disco manta sombrero gorra remera chomba camisa pollera calzoncillo puerta ventana vereda silla velador monitor teclado pantalla madera hierro acero vidrio zapato manada canguro dinosaurio esquina raqueta receta arena pared planta animal '
listaPalabras = sPalabras.split()
sI = randint(1, len(listaPalabras)-1)
palabra = listaPalabras[sI]
adivinada = ['*' for x in range(len(palabra))]
sAdivinada = ''.join(adivinada)
print('Adivine la palabra')
print(sAdivinada, len(sAdivinada), 'letras')
vidas = 5

win = False

while vidas > 0 and not win :
    print()
    print(vidas, 'vidas')
    bien = False
    letra = input('Letra: ')
       
    for x in range(len(palabra)):
        if palabra[x] == letra:
            adivinada[x] = letra
            bien = True

    if not bien:
        vidas -= 1
    sAdivinada = ''.join(adivinada)
    print(sAdivinada)
    if sAdivinada == palabra:
        win = True

if win:
    print('Seeeee')
else:
    print('Buuuuu, la palabra es', palabra)





