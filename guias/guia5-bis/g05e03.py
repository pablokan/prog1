# 3. Contar la cantidad de letras 

t = 'Quiero comer manzanas, solamente manzanas.'

def contarLetras(cadena):
    c = 0
    for l in cadena:
        if l not in ' ,.':
            c += 1
    return c

print(contarLetras(t))
print(contarLetras('Niño, andá a dormir.'))

