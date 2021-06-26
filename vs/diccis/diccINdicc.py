
pedido = {
    'lomo': {
        'mex': 500,
        'criollo': 450
    },
    'burger': {
        'american': 340,
        'blue': 410,
        'simple': 320
    }
}

print(pedido)

from pprint import pprint
pprint(pedido)

from json import dumps
print(dumps(pedido, indent=4))
