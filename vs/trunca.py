def trunc(r, d):
    s = str(r)
    posi = s.find(".")
    entero = s[:posi]
    decimales = s[posi+1:][:d]
    s = entero + "." + decimales
    r = float(s)
    return r

n = 3.141592
print(trunc(n,4))


