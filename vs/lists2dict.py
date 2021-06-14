nombres = ['Juan', 'Luisa', 'Ana']
edades = [31, 29, 56]

p = {}
for i, e in enumerate(nombres):
    p[e] = edades[i]
print(p)

q = {nombres[i]:edades[i] for i in range(len(nombres))} 
print(q)
