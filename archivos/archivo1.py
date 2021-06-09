f = open('qq.txt', 'w')
f.write("quico\nana\n")
lista = ['hola\n', 'chau\n']
f.writelines(lista)
f.close()

h = open('qq.txt', 'a')
h.write('agregado')





