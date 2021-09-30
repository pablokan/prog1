mano = [2, 1, 3, 1, 3, 10]
total1 = sum(mano)
total2 = 0
cartel = f"Total: {total1}"
if mano.count(1) != 0 and total1 + 10 < 22:
    total2 = total1 + 10
    cartel += f" o {total2}"
if total1 == 21 or total2 == 21:
    cartel = "Blackjack!"

print(cartel)
