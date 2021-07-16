import random

def milesNumGen():
    #generador de numero MILES
    c = 0
    numeroStr="11"
    while (len(set(numeroStr)) != 4):
        numeroStr=str(random.randint(1000,9999))
        c += 1
        print(c, numeroStr)
    return numeroStr

print(milesNumGen())
