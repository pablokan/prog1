a = open("kissling.txt", "r", encoding="utf8")
print("antes del read: ", a.tell())
primerosCaracteres = a.read(3)
print("despues del read: ", a.tell())
print(primerosCaracteres)
a.close()