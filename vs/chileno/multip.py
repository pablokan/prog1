def mult(a, b):
    if a < 0 and b < 0:
        a *= -1
        b *= -1
    elif b < 0:
        a, b = b, a
    t = 0
    for x in range(b):
        t += a
    return t

print(mult(5,-7))

