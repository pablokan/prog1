# Recibir por teclado una cadena de números e insertar
#  un punto cada 3 dígitos como divisorio de miles. 
# Ej.  1234567890 debería devolver 1.234.567.890

n = "1234567890"
c = 0
nn = ""
for i in range(len(n)):
    p = len(n) - 1 - i 
    nn = n[p] + nn
    c = c + 1
    if c == 3:
        nn = "." + nn
        c = 0

if nn[0] == ".":
    nn = nn[1:]

print(nn)




