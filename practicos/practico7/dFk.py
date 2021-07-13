print(list(map(int, ['1', '2'])))
print(list(map(len, ['hola', 'murciélago'])))

lista = 'a a b v d e a b c a b'.split()
print(dict.fromkeys(lista, 'nada'))

le = 'a A b v d e a B c a b'.split()
print(sorted(le))
print(sorted(le, key=lambda x: x.lower()))

l = lambda x:x*2

print(l(3))
print((lambda x:x*2)(4))
