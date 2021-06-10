# 5. Averiguar qué cantidad de letras tiene la palabra más larga.  
# Para ello, primero cargar cada palabra en una lista y 
# luego obtener la solicitada. Usar dos funciones.

texto = "Quiero comer manzanas, solamente manzanas."
soga = "hola pibe, como te va."

def armarLista(cadena):
    d = ''
    for l in cadena:
        if l not in ',.': # if l != ',' and l != '.'
            d += l
    return d.split(' ')

#print(armarLista(soga))

def masLarga(lista):
    c = 0
    for palabra in lista:
        if len(palabra) > c:
            c = len(palabra)
    return c

# print(masLarga(['hola', 'q', 'bernabeu', 'chau']))

print('La cantidad de letras de la palabra mas larga es',masLarga(armarLista(texto)))



