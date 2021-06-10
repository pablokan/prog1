# 2. Buscar una palabra y reemplazarla por otra 
# todas las veces que aparezca. 
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 
# 'Quiero comer peras, solamente peras.'

def reemplazar(vieja, nueva, cadena):
    while cadena.find(vieja) != -1:
        posVieja = cadena.find(vieja)
        inicio = cadena[:posVieja]
        final = cadena[posVieja+len(vieja):]
        cadena = inicio + nueva + final
    return cadena

t = 'Quiero comer manzanas, solamente manzanas.'

nuevaCadena = reemplazar('manzanas', 'peras', t)
print(t)
print(nuevaCadena)
print(reemplazar('Juan', 'Pablo', 'Hola Juan, como te va?'))

tt = t.replace('manzanas', 'uvas')
print(tt)


