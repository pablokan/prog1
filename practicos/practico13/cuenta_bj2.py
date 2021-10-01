mano = [2, 1, 3, 1, 3, 10]

def totales(mano):
    total = sum(mano)
    return total, total + 10 if mano.count(1) != 0 and total + 10 < 22 else total

print(totales(mano))
