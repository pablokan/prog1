orders = {
	'cappuccino': 54,
	'latte': 56,
	'Espresso': 72,
	'americano': 48,
	'cortado': 41
}

# si no lo diccionareo, el sorted me construye una lista de tuplas
sort_orders = dict(sorted(orders.items(), key=lambda x: x[0].lower(), reverse=True))
print(sort_orders)

for k, v in sort_orders.items():
    print(k, v, end='...')
