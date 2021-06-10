# 4. Contar la cantidad de palabras.
t = 'Quiero comer manzanas, solamente manzanas.'

def contarPalabras(cadena):
    return len(cadena.split(' '))

print(contarPalabras(t))
cade = 'Niño, hora de dormir. Es tarde, sabés?'
print(contarPalabras(cade))

