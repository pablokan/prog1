from calcula_edad import edad
f = open('personas.txt', 'r')

""" 
persona = ' '
while persona != '':
    persona = f.readline()
    if persona != '':
        persona = persona[:-1]
        fN = persona[-10:]
        if edad(fN) > 17:
            print(persona)
"""

personas = f.readlines()
for persona in personas:
    if edad(persona[-11:-1]) > 17:
        print(persona[:-13])

f.close()
