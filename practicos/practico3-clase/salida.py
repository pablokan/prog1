from calcula_edad import edad
f = open('data.txt', 'r')
personas = f.readlines()
f.close()
for persona in personas:
    nombre, fn = persona.split(' - ')
    fn = fn[:-1]
    if edad(fn) >= 18:
        print(nombre)



