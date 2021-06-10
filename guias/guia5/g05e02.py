# 2. Buscar una palabra y reemplazarla por otra todas las veces que aparezca. 
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

s = "Quiero comer manzanas, solamente manzanas."
v = "manzanas"
n = "peras"

def reemplazar(vieja, nueva, cadena):
    while cadena.find(vieja) != -1:
        posVieja = cadena.find(vieja)
        inicio = cadena[:posVieja]
        final = cadena[posVieja+len(vieja):]
        cadena = inicio + nueva + final
    return cadena

nuevaCadena = reemplazar(v, n, s)
print(nuevaCadena)

print(reemplazar('Boca', 'River', 'Boca es el mejor equipo de Argentina'))






