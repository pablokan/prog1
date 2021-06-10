# 5. Averiguar qué cantidad de letras tiene la palabra más larga.  
# Para ello, primero cargar cada palabra en una lista y luego 
# obtener la solicitada. Usar dos funciones.

t = 'Quiero comer manzanas, solamente manzanas.'

def armarLista(cadena):
    s = ''
    for l in cadena:
        if l not in ",.":
            s += l
    return s.split(' ')

def masLarga(lista):
    c = 0
    for palabra in lista:
        if len(palabra) > c:
            c = len(palabra)
    return c

print(masLarga(armarLista(t)))

