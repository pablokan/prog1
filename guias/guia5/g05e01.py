# 1. Cuántas veces se repite una letra cualquiera pedida. 
# Parámetros: letra, cadena.

def letterSearch(letter, string): 
    letterCount=0
    for e in string:
        if e==letter:
            letterCount=letterCount+1
    return letterCount

l=input("Que letra desea contar en la oracion: ")
s="Quiero comer manzanas, solamente manzanas"
#print(letterSearch('a','campana'))
print("La letra "+l+" se repite "+str(letterSearch(l,s))+" veces.")

