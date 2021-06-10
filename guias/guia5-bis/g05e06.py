# 6. Definir una lista de 10 posiciones con letras. 
# Contar las vocales y mostrar el total.

def contarVocales(lista):
    c = 0
    for l in lista:
        if l in 'aeiou':
            c += 1
    return c

print(contarVocales(['a', 'q', 'z', 'o', 'x']))
l = 'quiero fumar'
print(contarVocales(l))
