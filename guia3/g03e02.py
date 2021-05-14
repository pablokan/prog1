# Cargar letras en una lista (while). 
# Contar las vocales (for). Mostrar el total.

lista = 'qwertaayiop'
c = 0
for x in range(len(lista)):
    # if letra == 'a' or letra == 'e' etcetera
    if lista[x] in 'aeiou':
        c += 1

print(c)
