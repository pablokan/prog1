mano = [2, 1, 3, 1, 6]
total1 = sum([c for c in mano if c != 1]) + mano.count(1)
print(total1)

total2 = total1 + 10 if mano.count(1) != 0 else total1
cartel = f"Total: {total1}"
masCartel = f" o {total2}" if total1 != total2 else ""
print(cartel + masCartel)
