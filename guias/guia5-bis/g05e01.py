#1. Cuántas veces se repite una letra cualquiera pedida. 
# Parámetros: letra, cadena.
t = 'Quiero comer manzanas, solamente manzanas.'

def cantidad(letra, cadena):
    c = 0
    for l in cadena:
        if l == letra:
            c += 1
    return c

print(cantidad('a', t))
l = 'm'
print(cantidad(l, t))
canti = cantidad('e', 'Veamos que sale')
print(canti)

