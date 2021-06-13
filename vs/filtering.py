numbers = [1, -3, 10, -45, 6, 50]
print(list(filter(lambda x: x % 2 == 0, numbers))) # pares

# filter vs list comprehension
print(list(filter(lambda x: x > 0, numbers))) # positivos
print([x for x in numbers if x > 0]) # positivos


words = ["var", "file#", "head", "n$on", "2var"]
print(list(filter(str.isidentifier, words)))

# el cuadrado de los pares
print(list(map(lambda n: n ** 2, filter(lambda x: x % 2 == 0, numbers))))

