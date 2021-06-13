l = [x for x in range(10) if x % 2 == 1]
print(l)

sentence = 'the rocket came back from mars'
vowels = [i.upper() for i in sentence if i in 'aeiou']
print(vowels)

print(x := "Python")
print(type(x))